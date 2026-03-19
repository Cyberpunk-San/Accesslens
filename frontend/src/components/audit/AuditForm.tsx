'use client'

import { useMemo, useState } from 'react'
import { Search, Sparkles, SlidersHorizontal } from 'lucide-react'
import { Engine } from '@/lib/types'

interface AuditFormProps {
  url: string
  setUrl: (value: string) => void
  onStartAudit: (
    url: string,
    options: { engines: string[]; enableAI: boolean }
  ) => void
  isLoading?: boolean
  engines?: Engine[]
}

export function AuditForm({
  url,
  setUrl,
  onStartAudit,
  isLoading = false,
  engines = []
}: AuditFormProps) {
  const [showAdvanced, setShowAdvanced] = useState(false)
  const [enableAI, setEnableAI] = useState(true)

  const defaultEngineIds = useMemo(() => {
    if (!engines || engines.length === 0) return []

    return engines.map((engine: any, index) => {
      return (
        engine?.id?.toString?.() ||
        engine?.name?.toString?.() ||
        engine?.engine_id?.toString?.() ||
        `engine-${index}`
      )
    })
  }, [engines])

  return (
    <div className="rounded-[26px] border border-white/10 bg-black/35 p-4 md:p-5 backdrop-blur-xl shadow-[0_10px_40px_rgba(0,0,0,0.22)]">
      <div className="flex flex-col lg:flex-row gap-3 max-w-[750px] mx-auto">
        <div className="relative flex-1 min-w-0">
          
          <input
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter website URL for audit..."
            className="w-full pl-14 pr-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder:text-slate-400 outline-none focus:border-cyan-300/40 focus:ring-2 focus:ring-cyan-300/15"
          />
        </div>

        <button
          onClick={() =>
            onStartAudit(url, {
              engines: defaultEngineIds,
              enableAI
            })
          }
          className="px-6 py-3 rounded-xl bg-gradient-to-r from-purple-400 to-fuchsia-500 text-white font-semibold shadow-[0_0_30px_rgba(168,85,247,0.22)] hover:scale-[1.02] transition"
        >
          <span className="inline-flex items-center gap-2">
            <Sparkles size={16} />
            {isLoading ? 'Starting...' : 'Start Audit'}
          </span>
        </button>
      </div>

      <div className="mt-3 flex flex-col md:flex-row md:items-center md:justify-between gap-3">
        <button
          type="button"
          onClick={() => setShowAdvanced(!showAdvanced)}
          className="inline-flex w-fit items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-200 transition hover:border-cyan-300/30 hover:bg-white/10 hover:text-white"
        >
          <SlidersHorizontal size={16} />
          Advanced Configuration
        </button>

        <p className="text-xs text-slate-400">
          Available engines: {engines?.length || 0}
        </p>
      </div>

      {showAdvanced && (
        <div className="mt-4 rounded-2xl border border-white/10 bg-black/20 p-4 text-left">
          <label className="flex items-center gap-3 text-sm text-slate-200">
            <input
              type="checkbox"
              checked={enableAI}
              onChange={(e) => setEnableAI(e.target.checked)}
              className="h-4 w-4 accent-cyan-300"
            />
            Enable AI-assisted analysis
          </label>
        </div>
      )}
    </div>
  )
}