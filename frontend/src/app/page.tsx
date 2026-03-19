'use client'

import { useState } from 'react'
import { useQuery, useMutation } from '@tanstack/react-query'
import { api } from '@/lib/api'
import { useRouter } from 'next/navigation'
import { toast } from 'react-hot-toast'
import Link from 'next/link'
import {
  ShieldCheck,
  Zap,
  BarChart3,
  LayoutDashboard,
  FileSearch,
  History,
  Settings,
  Activity,
  Bell,
  UserCircle2,
  Sparkles,
} from 'lucide-react'

import { AuditForm } from '@/components/audit/AuditForm'
import { FeatureCard } from '@/components/audit/FeatureCard'
import { Engine } from '@/lib/types'

export default function HomePage() {
  const [url, setUrl] = useState('')
  const router = useRouter()

  const { data: engines } = useQuery<Engine[]>({
    queryKey: ['engines'],
    queryFn: api.getEngines,
  })

  const startAudit = useMutation({
    mutationFn: (request: {
      url: string
      engines: string[]
      enable_ai: boolean
    }) => api.startAudit(request),

    onSuccess: (data) => {
      toast.success('Audit started')
      router.push(`/audit/${data.audit_id}`)
    },

    onError: (error: Error) => {
      toast.error(error.message || 'No response from server')
    }
  })

  const handleStartAudit = (
    auditUrl: string,
    options: { engines: string[]; enableAI: boolean }
  ) => {
    if (!auditUrl.trim()) {
      toast.error('Enter URL')
      return
    }

    startAudit.mutate({
      url: auditUrl,
      engines: options.engines,
      enable_ai: options.enableAI
    })
  }

  return (
    <main className="min-h-screen flex">
      {/* SIDEBAR */}
      <aside className="hidden md:flex w-[250px] shrink-0 flex-col border-r border-white/10 bg-black/30 backdrop-blur-xl">
        <div className="px-6 py-7 border-b border-white/10">
          <h1 className="text-2xl font-bold text-white">AccessLens</h1>
          <p className="mt-2 text-sm text-slate-400">Accessibility intelligence</p>
        </div>

        <nav className="flex-1 px-4 py-6 space-y-2">
          <SidebarItem icon={<LayoutDashboard size={18} />} text="Dashboard" active />
          <SidebarItem icon={<FileSearch size={18} />} text="Start Audit" />
          <SidebarItem icon={<History size={18} />} text="Audit History" />
          <SidebarItem icon={<Activity size={18} />} text="Reports" />
          <SidebarItem icon={<Settings size={18} />} text="Settings" />
        </nav>

        <div className="px-4 pb-6">
          <div className="rounded-2xl border border-cyan-300/10 bg-white/5 p-4 backdrop-blur-xl">
            <p className="text-xs uppercase tracking-[0.18em] text-cyan-200">
              System status
            </p>
            <p className="mt-3 text-sm text-slate-300">
              Multi-engine accessibility auditing ready to deploy.
            </p>
          </div>
        </div>
      </aside>

      {/* MAIN */}
      <div className="flex-1 min-w-0">
        {/* TOP BAR */}
        <header className="border-b border-white/10 bg-black/20 backdrop-blur-xl">
          <div className="flex items-center justify-between px-5 md:px-8 py-4">
            <div>
              <p className="text-xs uppercase tracking-[0.22em] text-purple-300">
                WCAG Monitoring Console
              </p>
              <p className="mt-1 text-sm text-slate-300">Accessibility audit workspace</p>
            </div>

            <div className="flex items-center gap-4">
              <button className="rounded-full border border-white/10 bg-white/5 p-2.5 text-slate-300 transition hover:bg-white/10">
                <Bell size={18} />
              </button>

              <div className="flex items-center gap-3 rounded-full border border-white/10 bg-white/5 px-3 py-2">
                <UserCircle2 size={20} className="text-cyan-200" />
                <span className="text-sm text-slate-200">AccessLens Admin</span>
              </div>
            </div>
          </div>
        </header>

        <div className="px-5 md:px-8 py-8">
          {/* HERO */}
          <section className="rounded-[30px] border border-white/10 bg-gradient-to-r from-[#140428] via-[#21074c] to-[#10213d] p-6 md:p-8 xl:p-10 shadow-[0_0_90px_rgba(168,85,247,0.16)]">
            <div className="grid gap-8 xl:grid-cols-[1.35fr_0.85fr] xl:items-start">
              {/* LEFT / MAIN HERO CONTENT */}
              <div className="min-w-0 xl:text-left text-center">
                <div className="inline-flex items-center gap-2 rounded-full border border-cyan-300/15 bg-white/10 px-4 py-2 text-sm text-cyan-100">
                  <Sparkles size={14} />
                  Protocol AccessLens
                </div>

                <h1 className="mt-6 text-4xl md:text-5xl xl:text-6xl font-bold leading-tight text-white">
                  Accessibility auditing,
                  <span className="block bg-gradient-to-r from-purple-300 via-fuchsia-300 to-cyan-300 bg-clip-text text-transparent">
                    rebuilt for modern teams.
                  </span>
                </h1>

                <p className="mt-5 max-w-3xl xl:mx-0 mx-auto text-base md:text-lg leading-8 text-slate-300">
                  Automate WCAG checks, combine multiple engines, and surface high-impact
                  accessibility issues with a premium workflow built for real product teams.
                </p>

                <div className="mt-8 max-w-3xl xl:mx-0 mx-auto">
                  <AuditForm
                    url={url}
                    setUrl={setUrl}
                    onStartAudit={handleStartAudit}
                    isLoading={startAudit.isPending}
                    engines={engines}
                  />
                </div>

                <div className="mt-5 flex flex-wrap gap-3 xl:justify-start justify-center">
                  <Link
                    href="/dashboard"
                    className="inline-flex items-center rounded-full border border-cyan-300/20 bg-cyan-300/10 px-5 py-2.5 text-cyan-100 backdrop-blur-xl transition hover:border-cyan-300/40 hover:bg-cyan-300/15 hover:text-white"
                  >
                    Open Access Intelligence Dashboard →
                  </Link>

                  <button
                    type="button"
                    className="inline-flex items-center rounded-full border border-white/10 bg-white/5 px-5 py-2.5 text-slate-200 transition hover:bg-white/10"
                  >
                    View reports
                  </button>
                </div>
              </div>

              {/* STATS */}
              <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-1">
                <StatCard
                  label="Active Engines"
                  value={engines?.length || 0}
                  sub="scan modules online"
                />
                <StatCard
                  label="Audit Status"
                  value={startAudit.isPending ? 'Live' : 'Ready'}
                  sub={startAudit.isPending ? 'audit in progress' : 'ready for next run'}
                />
                <StatCard
                  label="AI Analysis"
                  value="Enabled"
                  sub="assisted accessibility review"
                />
              </div>
            </div>
          </section>

          {/* FEATURES */}
          <section className="mt-12 ml-2 md:ml-4">
            <div className="text-center">
              <p className="text-sm uppercase tracking-[0.25em] text-cyan-200">
                Platform capabilities
              </p>

              <h2 className="mt-4 text-3xl md:text-4xl xl:text-5xl font-semibold text-white">
                Built for high-confidence accessibility reviews
              </h2>

              <p className="mx-auto mt-4 max-w-2xl text-slate-300 leading-7">
                From policy checks to visual intelligence, AccessLens gives teams a
                unified audit surface with faster analysis and better visibility.
              </p>
            </div>

            <div className="mt-10 grid gap-6 md:grid-cols-3">
              <FeatureCard
                icon={<ShieldCheck size={24} />}
                title="Policy Enforcement"
                description="Automated WCAG validation engine detecting accessibility violations across the page."
              />

              <FeatureCard
                icon={<Zap size={24} />}
                title="Instant Synthesis"
                description="Parallel accessibility engine execution for faster audit results."
              />

              <FeatureCard
                icon={<BarChart3 size={24} />}
                title="Visual Intelligence"
                description="AI + computer vision analysis for layout, semantics, and contrast issues."
              />
            </div>
          </section>
        </div>
      </div>
    </main>
  )
}

function SidebarItem({
  icon,
  text,
  active = false,
}: {
  icon: React.ReactNode
  text: string
  active?: boolean
}) {
  return (
    <button
      className={`flex w-full items-center gap-3 rounded-2xl px-4 py-3 text-left transition ${
        active
          ? 'bg-gradient-to-r from-purple-500/30 to-cyan-400/12 text-white border border-white/10'
          : 'text-slate-300 hover:bg-white/5 hover:text-white'
      }`}
    >
      <span>{icon}</span>
      <span className="text-sm font-medium">{text}</span>
    </button>
  )
}

function StatCard({
  label,
  value,
  sub,
}: {
  label: string
  value: string | number
  sub: string
}) {
  return (
    <div className="rounded-3xl border border-cyan-300/10 bg-black/20 p-5 backdrop-blur-xl shadow-[0_0_35px_rgba(34,211,238,0.05)]">
      <p className="text-xs uppercase tracking-[0.18em] text-slate-300">
        {label}
      </p>
      <p className="mt-4 text-3xl font-semibold text-white break-words">
        {value}
      </p>
      <p className="mt-2 text-sm text-slate-300">
        {sub}
      </p>
    </div>
  )
}