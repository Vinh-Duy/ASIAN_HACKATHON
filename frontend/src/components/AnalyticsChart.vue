<template>
  <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
    <h2 class="text-lg font-bold mb-6 text-slate-100">Field Analysis</h2>
    
    <div class="space-y-6">
      <div class="grid grid-cols-2 gap-4">
        <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
          <div class="text-slate-400 text-sm mb-1">Soil Moisture</div>
          <div class="text-3xl font-bold text-blue-400">{{ field.soil_moisture }}%</div>
          <div class="text-xs text-slate-500 mt-2">Current level</div>
        </div>
        <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
          <div class="text-slate-400 text-sm mb-1">Water Deficit</div>
          <div class="text-3xl font-bold text-orange-400">{{ field.water_deficit }}L</div>
          <div class="text-xs text-slate-500 mt-2">Per hectare needed</div>
        </div>
      </div>

      <div class="h-40 bg-slate-900/30 rounded-lg border border-slate-600 p-4">
        <div class="w-full h-full flex items-end gap-1 justify-center">
          <div v-for="i in 24" :key="i" class="flex-1 bg-gradient-to-t from-green-400 to-emerald-300 rounded-t opacity-70" :style="{ height: (Math.random() * 80 + 20) + '%' }"></div>
        </div>
      </div>

      <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
        <h3 class="text-sm font-bold text-slate-200 mb-3">Recommendation</h3>
        <p class="text-emerald-400 text-sm">💧 Optimal: Tưới 15L/cây vào 5h chiều. Hệ thống sẽ tự động mở van.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  field: Object
})
</script>
