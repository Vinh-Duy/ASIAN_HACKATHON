<template>
  <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
    <h2 class="text-lg font-bold mb-6 text-slate-100">🌤️ Weather & Forecast</h2>
    
    <div class="space-y-6">
      <!-- Current Weather -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
          <div class="text-slate-400 text-xs mb-2">TEMPERATURE</div>
          <div class="text-2xl font-bold text-orange-400">32.5°C</div>
        </div>
        <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
          <div class="text-slate-400 text-xs mb-2">HUMIDITY</div>
          <div class="text-2xl font-bold text-blue-400">65%</div>
        </div>
        <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
          <div class="text-slate-400 text-xs mb-2">WIND SPEED</div>
          <div class="text-2xl font-bold text-cyan-400">2.3 m/s</div>
        </div>
        <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
          <div class="text-slate-400 text-xs mb-2">RAIN CHANCE</div>
          <div class="text-2xl font-bold text-slate-300">15%</div>
        </div>
      </div>

      <!-- 7-Day Forecast -->
      <div class="bg-slate-900/30 rounded-lg border border-slate-600 p-4">
        <h3 class="text-sm font-bold text-slate-200 mb-4">7-Day Forecast</h3>
        <div class="grid grid-cols-7 gap-2">
          <div v-for="day in 7" :key="day" class="text-center">
            <div class="text-xs text-slate-400 mb-2">{{ ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][day - 1] }}</div>
            <div class="bg-slate-800 rounded-lg p-3 border border-slate-600">
              <div class="text-2xl mb-2">{{ ['☀️', '⛅', '☁️', '🌧️'][Math.floor(Math.random() * 4)] }}</div>
              <div class="text-sm font-bold text-orange-400">{{ 28 + Math.floor(Math.random() * 6) }}°</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Alert -->
      <div class="bg-yellow-900/20 border border-yellow-700 rounded-lg p-4">
        <div class="flex gap-3">
          <span class="text-xl">⚠️</span>
          <div>
            <h4 class="font-bold text-yellow-300 mb-1">Forecast Alert</h4>
            <p class="text-sm text-yellow-200">No rain expected for 3 days. Consider irrigation in next 24 hours.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  field: Object
})
</script>
