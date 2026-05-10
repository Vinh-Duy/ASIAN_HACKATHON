<template>
  <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
    <h2 class="text-lg font-bold mb-6 text-slate-100">💧 Irrigation Control</h2>
    
    <div class="space-y-6">
      <!-- Valve Status -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-slate-900/50 rounded-lg p-6 border border-slate-600">
          <div class="text-slate-400 text-sm mb-2">VALVE STATUS</div>
          <div class="flex items-center gap-3 mb-4">
            <div class="w-4 h-4 bg-green-500 rounded-full animate-pulse"></div>
            <span class="text-xl font-bold text-green-400">CLOSED</span>
          </div>
          <div class="text-xs text-slate-400">Last activity: 2 hours ago</div>
        </div>
        <div class="bg-slate-900/50 rounded-lg p-6 border border-slate-600">
          <div class="text-slate-400 text-sm mb-2">WATER FLOW</div>
          <div class="text-3xl font-bold text-blue-400 mb-4">0 L/h</div>
          <div class="text-xs text-slate-400">Flow rate when active</div>
        </div>
      </div>

      <!-- Control Buttons -->
      <div class="grid grid-cols-2 gap-4">
        <button
          @click="startIrrigation"
          :disabled="isIrrigating"
          class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-700 hover:to-emerald-700 disabled:from-slate-600 disabled:to-slate-600 text-white font-bold rounded-lg transition-all transform hover:scale-105"
        >
          {{ isIrrigating ? '⏹️ Stop' : '▶️ Start Irrigation' }}
        </button>
        <button
          @click="triggerAutomatic"
          class="px-6 py-3 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white font-bold rounded-lg transition-all transform hover:scale-105"
        >
          🤖 Auto Mode
        </button>
      </div>

      <!-- Duration Selector -->
      <div class="bg-slate-900/50 rounded-lg p-4 border border-slate-600">
        <label class="block text-sm text-slate-300 mb-2">Duration (minutes)</label>
        <input
          v-model.number="duration"
          type="range"
          min="5"
          max="120"
          step="5"
          class="w-full"
        />
        <div class="flex justify-between text-xs text-slate-400 mt-2">
          <span>5 min</span>
          <span class="text-green-400 font-bold">{{ duration }} min</span>
          <span>120 min</span>
        </div>
      </div>

      <!-- Active Irrigation Display -->
      <div v-if="isIrrigating" class="bg-green-900/20 border border-green-700 rounded-lg p-4">
        <div class="flex gap-3">
          <span class="text-2xl animate-bounce">💧</span>
          <div class="flex-1">
            <h4 class="font-bold text-green-300 mb-2">Irrigation Active</h4>
            <div class="space-y-1 text-sm text-green-200">
              <p>Duration: {{ duration }} minutes</p>
              <p>Estimated water: {{ (duration * 50 / 60).toFixed(0) }}L</p>
              <p>Started: Just now</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Schedule -->
      <div class="bg-slate-900/30 rounded-lg border border-slate-600 p-4">
        <h3 class="font-bold text-slate-200 mb-3">📅 Schedule</h3>
        <div class="space-y-2 text-sm">
          <div class="flex justify-between items-center">
            <span class="text-slate-400">Today 5:00 PM</span>
            <span class="text-emerald-400 font-bold">15L planned</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-slate-400">Tomorrow 5:00 PM</span>
            <span class="text-emerald-400 font-bold">12L planned</span>
          </div>
        </div>
      </div>

      <!-- Water Savings -->
      <div class="bg-gradient-to-r from-emerald-900/30 to-cyan-900/30 rounded-lg border border-emerald-700 p-4">
        <div class="flex gap-3">
          <span class="text-2xl">♻️</span>
          <div>
            <h4 class="font-bold text-emerald-300">Water Saved This Month</h4>
            <p class="text-lg font-bold text-emerald-400">45,000 L</p>
            <p class="text-xs text-emerald-200">vs. traditional irrigation (40% more efficient)</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  field: Object
})

const isIrrigating = ref(false)
const duration = ref(30)

const startIrrigation = () => {
  isIrrigating.value = !isIrrigating.value
  if (!isIrrigating.value) {
    alert('Irrigation stopped!')
  }
}

const triggerAutomatic = () => {
  alert('🤖 Auto mode activated! System will handle irrigation based on soil moisture.')
}
</script>

<style scoped>
input[type="range"] {
  accent-color: #10b981;
}
</style>
