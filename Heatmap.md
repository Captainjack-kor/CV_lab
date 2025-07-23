import React from 'react';
import { Box, Grid, Typography, Paper } from '@mui/material';

const heatmapData = {
  'M': { '6am': 1, '10am': 3, '12pm': 0, '5pm': 5, '8pm': 0 },
  'T': { '6am': 2, '10am': 4, '12pm': 2, '5pm': 0, '8pm': 0 },
  'W': { '6am': 0, '10am': 0, '12pm': 3, '5pm': 4, '8pm': 0 },
  'T': { '6am': 4, '10am': 5, '12pm': 5, '5pm': 2, '8pm': 0 },
  'F': { '6am': 1, '10am': 3, '12pm': 4, '5pm': 1, '8pm': 0 },
  'S': { '6am': 0, '10am': 0, '12pm': 0, '5pm': 0, '8pm': 3 },
  'S': { '6am': 0, '10am': 0, '12pm': 0, '5pm': 0, '8pm': 5 },
};

const days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']; // 월, 화, 수, 목, 금, 토, 일
const times = ['6am', '10am', '12pm', '5pm', '8pm']; // 시간대

// 값에 따라 색상 강도를 결정하는 헬퍼 함수 (예시)
const getColorIntensity = (value) => {
  if (value === 0) return '#e0e0e0'; // 가장 연한 회색 (활동 없음)
  if (value === 1) return '#bbdefb'; // 연한 파란색
  if (value <= 2) return '#90caf9';
  if (value <= 3) return '#64b5f6';
  if (value <= 4) return '#42a5f5';
  if (value >= 5) return '#2196f3'; // 가장 진한 파란색 (활동 많음)
  return '#e0e0e0';
};

export default function CustomHeatmapGrid() {
  return (
    <Box sx={{ p: 4, bgcolor: 'background.paper', borderRadius: 2, boxShadow: 3 }}>
      <Typography variant="h6" gutterBottom>
        Issues opening time
      </Typography>
      <Grid container spacing={0.5} sx={{ width: 'fit-content' }}>
        {/* 시간대 레이블 */}
        <Grid item xs={12}>
          <Box sx={{ display: 'flex' }}>
            <Box sx={{ width: '40px', height: '30px' }}></Box> {/* 빈 칸 */}
            {days.map((day, index) => (
              <Box key={index} sx={{ width: '40px', height: '30px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <Typography variant="caption" sx={{ fontWeight: 'bold' }}>{day}</Typography>
              </Box>
            ))}
          </Box>
        </Grid>

        {/* 히트맵 그리드 */}
        {times.map((time, timeIndex) => (
          <Grid item xs={12} key={timeIndex}>
            <Box sx={{ display: 'flex' }}>
              {/* 시간 레이블 */}
              <Box sx={{ width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'flex-end', pr: 1 }}>
                <Typography variant="caption" sx={{ fontWeight: 'bold' }}>{time}</Typography>
              </Box>
              {/* 데이터 셀 */}
              {days.map((day, dayIndex) => {
                const value = heatmapData[day][time] || 0; // 해당 데이터가 없으면 0
                return (
                  <Paper
                    key={`${day}-${time}`}
                    sx={{
                      width: '40px',
                      height: '40px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      bgcolor: getColorIntensity(value), // 값에 따라 배경색 변경
                      borderRadius: 1,
                      transition: 'background-color 0.3s ease-in-out',
                      '&:hover': {
                        opacity: 0.8,
                      }
                    }}
                    title={`요일: ${day}, 시간: ${time}, 값: ${value}`} // 툴팁
                  >
                    {/* 필요하다면 여기에 값 표시 (선택 사항) */}
                    {/* <Typography variant="caption" sx={{ color: 'white' }}>{value}</Typography> */}
                  </Paper>
                );
              })}
            </Box>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}
