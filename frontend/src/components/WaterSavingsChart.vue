<template>
  <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur">
    <h2 class="text-xl font-bold text-white mb-6">💧 Water Savings Analytics</h2>
    
    <!-- Comparison Chart -->
    <div class="mb-8">
      <h3 class="text-sm font-semibold text-slate-300 mb-4">This Month Comparison</h3>
      <div class="flex items-end gap-8 justify-around">
        <!-- Traditional Method -->
        <div class="flex flex-col items-center">
          <div class="w-16 bg-gradient-to-t from-orange-500 to-orange-400 rounded-lg" 
               :style="{ height: traditionalBar + '%' }"></div>
          <div class="text-xs text-slate-400 mt-2">Traditional</div>
          <div class="text-lg font-bold text-orange-400 mt-1">{{ traditionalUsage }}L</div>
        </div>
        
        <!-- AgriDrop Method -->
        <div class="flex flex-col items-center">
          <div class="w-16 bg-gradient-to-t from-green-500 to-emerald-400 rounded-lg" 
               :style="{ height: agridropBar + '%' }"></div>
          <div class="text-xs text-slate-400 mt-2">AgriDrop</div>
          <div class="text-lg font-bold text-emerald-400 mt-1">{{ agridropUsage }}L</div>
        </div>
      </div>
      
      <!-- Savings Badge -->
      <div class="mt-8 bg-gradient-to-r from-green-500/20 to-emerald-500/20 border border-emerald-500/50 rounded-lg p-4 text-center">
        <div class="text-3xl font-bold text-emerald-400">{{ savingsPercentage }}%</div>
        <div class="text-sm text-emerald-300">Water Reduction</div>
      </div>
    </div>

    <!-- Detailed Metrics -->
    <div class="grid grid-cols-2 gap-4 mb-6">
      <!-- Cost Savings -->
      <div class="bg-slate-700/30 rounded-lg p-4 border border-slate-600">
        <div class="text-sm text-slate-400 mb-2">💰 Monthly Cost Savings</div>
        <div class="text-2xl font-bold text-green-400">${{ costSavings }}/month</div>
        <div class="text-xs text-slate-500 mt-1">Per average farm</div>
      </div>
      
      <!-- CO₂ Reduction -->
      <div class="bg-slate-700/30 rounded-lg p-4 border border-slate-600">
        <div class="text-sm text-slate-400 mb-2">🌍 CO₂ Emissions Reduced</div>
        <div class="text-2xl font-bold text-blue-400">{{ co2Reduced }}kg</div>
        <div class="text-xs text-slate-500 mt-1">Monthly per farm</div>
      </div>
    </div>

    <!-- Impact Metrics -->
    <div class="bg-slate-700/30 rounded-lg p-4 border border-slate-600">
      <div class="text-sm font-semibold text-slate-300 mb-3">Scalability Impact (500K farms)</div>
      <div class="space-y-2">
        <div class="flex justify-between items-center">
          <span class="text-sm text-slate-400">Water Saved Annually</span>
          <span class="text-sm font-bold text-emerald-400">{{ waterSavedScaled }}B liters</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-sm text-slate-400">Cost Savings</span>
          <span class="text-sm font-bold text-green-400">${{ costSavingsScaled }}M</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-sm text-slate-400">CO₂ Reduction</span>
          <span class="text-sm font-bold text-blue-400">{{ co2ReducedScaled }}M tons</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-sm text-slate-400">Farms Supported</span>
          <span class="text-sm font-bold text-purple-400">500,000+</span>
        </div>
      </div>
    </div>

    <!-- Monthly Trend -->
    <div class="mt-6 pt-6 border-t border-slate-700">
      <h3 class="text-sm font-semibold text-slate-300 mb-4">Savings Trend (Last 6 Months)</h3>
      <div class="space-y-2">
        <div v-for="month in monthlyTrend" :key="month.name" class="flex items-center gap-3">
          <span class="text-xs text-slate-400 w-10">{{ month.name }}</span>
          <div class="flex-1 bg-slate-700/50 rounded-full h-2">
            <div class="bg-gradient-to-r from-emerald-400 to-green-500 h-2 rounded-full" 
                 :style="{ width: (month.value / 50) + '%' }"></div>
          </div>
          <span class="text-xs font-bold text-emerald-400 w-12 text-right">{{ month.value }}%</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WaterSavingsChart',
  data() {
    return {
      // Monthly comparison
      traditionalUsage: 1200000,  // liters
      agridropUsage: 720000,       // liters (40% reduction)
      savingsPercentage: 40,
      
      // Cost and environment metrics
      costSavings: 450,            // $ per month per farm
      co2Reduced: 125,             // kg per month per farm
      
      // Scaled metrics (500K farms)
      waterSavedScaled: 22.5,      // Billion liters per year
      costSavingsScaled: 225,      // Million $ per year
      co2ReducedScaled: 7.5,       // Million tons per year
      
      // Visual bars
      traditionalBar: 100,
      agridropBar: 60,             // 60% of traditional = 40% reduction
      
      // Trend data
      monthlyTrend: [
        { name: 'May', value: 35 },
        { name: 'Apr', value: 32 },
        { name: 'Mar', value: 28 },
        { name: 'Feb', value: 25 },
        { name: 'Jan', value: 18 },
        { name: 'Dec', value: 15 },
      ]
    }
  }
}
</script>

<style scoped>
</style>
