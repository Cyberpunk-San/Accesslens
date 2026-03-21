# 1. Build Stage
FROM node:20 AS builder

WORKDIR /app

# Only copy package.json to avoid the npm native binding bug (https://github.com/npm/cli/issues/4828)
COPY package.json ./

# Install dependencies from scratch for the Linux environment
# Increased timeouts to handle unstable network connections
RUN npm config set fetch-retry-maxtimeout 600000 && \
    npm config set fetch-retries 5 && \
    npm install

# Copy the rest of the application code
COPY . .

# Set environment variables for the build
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}

# Build the Next.js application
RUN npm run build

# 2. Production Stage
FROM node:20 AS runner

WORKDIR /app

ENV NODE_ENV=production

# Copy necessary files from the builder stage
# We use the standard Next.js start method since the user preferred it
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

# Start the Next.js application
CMD ["npm", "start"]
