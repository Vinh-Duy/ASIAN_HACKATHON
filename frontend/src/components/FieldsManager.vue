<template>
  <div class="space-y-4">
    <!-- Create Field Form -->
    <div v-if="!showForm" class="flex gap-2">
      <button
        @click="showForm = true"
        class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors font-medium"
      >
        + Add New Field
      </button>
    </div>

    <div v-else class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
      <h3 class="text-lg font-bold mb-4 text-slate-100">Create New Field</h3>
      <div class="space-y-4">
        <input
          v-model="formData.name"
          placeholder="Field Name"
          class="w-full px-4 py-2 bg-slate-900 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:border-green-500 outline-none"
        />
        <div class="grid grid-cols-2 gap-4">
          <input
            v-model.number="formData.latitude"
            placeholder="Latitude"
            type="number"
            step="0.0001"
            class="px-4 py-2 bg-slate-900 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:border-green-500 outline-none"
          />
          <input
            v-model.number="formData.longitude"
            placeholder="Longitude"
            type="number"
            step="0.0001"
            class="px-4 py-2 bg-slate-900 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:border-green-500 outline-none"
          />
        </div>
        <div class="grid grid-cols-2 gap-4">
          <input
            v-model.number="formData.area_hectares"
            placeholder="Area (hectares)"
            type="number"
            class="px-4 py-2 bg-slate-900 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:border-green-500 outline-none"
          />
          <select
            v-model="formData.crop_type"
            class="px-4 py-2 bg-slate-900 border border-slate-600 rounded-lg text-white focus:border-green-500 outline-none"
          >
            <option value="coffee">Coffee ☕</option>
            <option value="durian">Durian 🍌</option>
          </select>
        </div>
        <div class="flex gap-2">
          <button
            @click="createField"
            class="flex-1 px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors font-medium"
          >
            Create Field
          </button>
          <button
            @click="showForm = false"
            class="flex-1 px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-lg transition-colors"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>

    <!-- Fields List -->
    <div class="space-y-3">
      <div
        v-for="field in fieldsList"
        :key="field.field_id"
        @click="$emit('field-selected', field)"
        class="bg-slate-800/50 border border-slate-700 rounded-lg p-4 backdrop-blur cursor-pointer hover:border-green-500 transition-colors"
      >
        <div class="flex items-center justify-between mb-2">
          <h3 class="font-bold text-slate-100">{{ field.name }}</h3>
          <span class="text-xs bg-green-900/50 text-green-300 px-2 py-1 rounded">{{ field.crop_type }}</span>
        </div>
        <div class="grid grid-cols-3 gap-2 text-sm text-slate-400">
          <div>📍 {{ field.latitude.toFixed(2) }}°, {{ field.longitude.toFixed(2) }}°</div>
          <div>📏 {{ field.area_hectares }} ha</div>
          <div class="text-right">💧 {{ field.soil_moisture || 65 }}%</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

const emit = defineEmits(['field-selected'])

const showForm = ref(false)
const fieldsList = ref([
  {
    field_id: '1',
    name: 'Field A - Coffee',
    latitude: 12.6667,
    longitude: 108.0333,
    area_hectares: 5,
    crop_type: 'coffee',
    soil_moisture: 65
  }
])

const formData = ref({
  name: '',
  latitude: 12.6667,
  longitude: 108.0333,
  area_hectares: 5,
  crop_type: 'coffee'
})

const createField = async () => {
  try {
    // In production, call API: await axios.post('/api/v1/fields', formData.value)
    const newField = {
      field_id: Date.now().toString(),
      ...formData.value,
      soil_moisture: 65
    }
    fieldsList.value.push(newField)
    showForm.value = false
    formData.value = { name: '', latitude: 12.6667, longitude: 108.0333, area_hectares: 5, crop_type: 'coffee' }
    emit('field-selected', newField)
  } catch (error) {
    console.error('Error creating field:', error)
  }
}
</script>
