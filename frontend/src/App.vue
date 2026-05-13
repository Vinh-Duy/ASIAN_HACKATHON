<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
    <!-- Header -->
    <header class="border-b border-slate-700 bg-slate-800/50 backdrop-blur sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-br from-green-400 to-emerald-600 rounded-lg flex items-center justify-center">
            <span class="text-xl font-bold text-white">🌾</span>
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent">
            AgriDrop
          </h1>
        </div>
        <div class="text-sm text-slate-400">
          Smart Precision Irrigation System
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-6 py-8">
      <!-- Quick Stats -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
          <div class="text-slate-400 text-sm mb-2">Active Fields</div>
          <div class="text-3xl font-bold text-green-400">{{ fields.length }}</div>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
          <div class="text-slate-400 text-sm mb-2">Avg Soil Moisture</div>
          <div class="text-3xl font-bold text-blue-400">{{ avgMoisture }}%</div>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
          <div class="text-slate-400 text-sm mb-2">Water Saved</div>
          <div class="text-3xl font-bold text-emerald-400">{{ waterSaved }}L</div>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
          <div class="text-slate-400 text-sm mb-2">System Status</div>
          <div class="text-2xl font-bold text-emerald-400">✓ Operational</div>
        </div>
      </div>

      <!-- Tabs -->
      <div class="flex gap-4 mb-6 border-b border-slate-700">
        <button
          v-for="tab in tabs"
          :key="tab"
          @click="activeTab = tab"
          :class="[
            'px-4 py-2 text-sm font-medium transition-all',
            activeTab === tab
              ? 'text-green-400 border-b-2 border-green-400'
              : 'text-slate-400 hover:text-slate-300'
          ]"
        >
          {{ tab }}
        </button>
      </div>

      <!-- Tab Content -->
      <div class="space-y-6">
        <!-- Dashboard Tab -->
        <div v-if="activeTab === 'Dashboard'" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <!-- Map -->
          <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur overflow-hidden">
            <h2 class="text-lg font-bold mb-4 text-slate-100">Field Locations</h2>
            <div class="h-80 bg-slate-900/50 rounded border border-slate-600 flex items-center justify-center text-slate-400">
              <MapContainer v-if="fields.length > 0" :fields="fields" />
              <div v-else class="text-center">
                <p>No fields added yet. Create a field to get started.</p>
              </div>
            </div>
          </div>

          <!-- Analytics -->
          <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
            <h2 class="text-lg font-bold mb-4 text-slate-100">Today's Analysis</h2>
            <AnalyticsChart v-if="selectedField" :field="selectedField" />
            <div v-else class="text-slate-400 text-center py-20">
              Select a field from the list to view analytics
            </div>
          </div>
        </div>

        <!-- Fields Tab -->
        <div v-if="activeTab === 'Fields'">
          <FieldsManager @field-selected="selectedField = $event" />
        </div>

        <!-- Weather Tab -->
        <div v-if="activeTab === 'Weather'">
          <WeatherWidget v-if="selectedField" :field="selectedField" />
          <div v-else class="text-center text-slate-400 py-20">
            Select a field to view weather data
          </div>
        </div>

        <!-- Irrigation Tab -->
        <div v-if="activeTab === 'Irrigation'">
          <IrrigationControl v-if="selectedField" :field="selectedField" />
          <div v-else class="text-center text-slate-400 py-20">
            Select a field to control irrigation
          </div>
        </div>

        <!-- Impact Tab -->
        <div v-if="activeTab === 'Impact'">
          <WaterSavingsChart />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import MapContainer from './components/MapContainer.vue'
import AnalyticsChart from './components/AnalyticsChart.vue'
import FieldsManager from './components/FieldsManager.vue'
import WeatherWidget from './components/WeatherWidget.vue'
import IrrigationControl from './components/IrrigationControl.vue'
import WaterSavingsChart from './components/WaterSavingsChart.vue'

const activeTab = ref('Dashboard')
const tabs = ['Dashboard', 'Fields', 'Weather', 'Irrigation', 'Impact']
const fields = ref([
  {
    field_id: '1',
    name: 'Field A - Coffee',
    latitude: 12.6667,
    longitude: 108.0333,
    area_hectares: 5,
    crop_type: 'coffee',
    soil_moisture: 65,
    water_deficit: 12.5
  }
])
const selectedField = ref(fields.value[0])

const avgMoisture = computed(() => {
  if (fields.value.length === 0) return 0
  const sum = fields.value.reduce((acc, f) => acc + (f.soil_moisture || 0), 0)
  return Math.round(sum / fields.value.length)
})

const waterSaved = computed(() => {
  return Math.round(fields.value.length * 45000)
})
</script>
