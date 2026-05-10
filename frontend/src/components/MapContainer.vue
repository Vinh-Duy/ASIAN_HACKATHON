<template>
  <div class="h-80 bg-gradient-to-br from-slate-900 to-slate-800 rounded-lg border border-slate-600 relative overflow-hidden">
    <svg class="absolute inset-0 w-full h-full" viewBox="0 0 400 300">
      <!-- Grid -->
      <g stroke="#475569" stroke-width="0.5" opacity="0.3">
        <line x1="0" y1="50" x2="400" y2="50" />
        <line x1="0" y1="100" x2="400" y2="100" />
        <line x1="0" y1="150" x2="400" y2="150" />
        <line x1="0" y1="200" x2="400" y2="200" />
        <line x1="0" y1="250" x2="400" y2="250" />
      </g>

      <!-- Fields as circles -->
      <circle
        v-for="(field, idx) in fields"
        :key="field.field_id"
        :cx="50 + idx * 100"
        :cy="150"
        r="25"
        :fill="getMoistureColor(field.soil_moisture)"
        opacity="0.8"
        stroke="white"
        stroke-width="2"
      />
    </svg>

    <!-- Legend -->
    <div class="absolute bottom-4 left-4 right-4 flex gap-4 text-xs">
      <div class="flex items-center gap-2">
        <div class="w-4 h-4 bg-green-500 rounded-full"></div>
        <span class="text-slate-300">Optimal (>60%)</span>
      </div>
      <div class="flex items-center gap-2">
        <div class="w-4 h-4 bg-yellow-500 rounded-full"></div>
        <span class="text-slate-300">Moderate (30-60%)</span>
      </div>
      <div class="flex items-center gap-2">
        <div class="w-4 h-4 bg-red-500 rounded-full"></div>
        <span class="text-slate-300">Critical (<30%)</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  fields: Array
})

const getMoistureColor = (moisture) => {
  if (moisture > 60) return '#10b981'
  if (moisture > 30) return '#eab308'
  return '#ef4444'
}
</script>
