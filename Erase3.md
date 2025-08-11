import React, { useState, useEffect, useRef } from 'react';
import { createSwapy } from 'swapy';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';

// 컬럼 헤더에 대한 데이터
const initialColumns = [
  { id: '1', name: '컬럼 1' },
  { id: '2', name: '컬럼 2' },
  { id: '3', name: '컬럼 3' },
  { id: '4', name: '컬럼 4' },
];

const rows = [
  { id: 1, col1: 'Row 1-1', col2: 'Row 1-2', col3: 'Row 1-3', col4: 'Row 1-4' },
  { id: 2, col1: 'Row 2-1', col2: 'Row 2-2', col3: 'Row 2-3', col4: 'Row 2-4' },
  { id: 3, col1: 'Row 3-1', col2: 'Row 3-2', col3: 'Row 3-3', col4: 'Row 3-4' },
];

export default function SwapyTable() {
  const [columns, setColumns] = useState(initialColumns);
  const containerRef = useRef(null);
  const swapyRef = useRef(null);

  useEffect(() => {
    if (containerRef.current) {
      // Swapy 인스턴스 생성
      swapyRef.current = createSwapy(containerRef.current, {
        // 드래그 가능한 아이템과 슬롯을 지정하기 위한 데이터 속성
        itemClass: 'swapy-item',
        slotClass: 'swapy-slot',
        dragAxis: 'x', // 수평 드래그만 허용
      });

      // 스왑이 완료되었을 때 호출되는 이벤트
      swapyRef.current.onSwapEnd((event) => {
        if (event.hasChanged) {
          const newColumnOrder = event.newOrder.map(item => {
            const originalColumn = initialColumns.find(col => `swapy-item-${col.id}` === item.id);
            return originalColumn;
          });
          setColumns(newColumnOrder);
        }
      });
    }

    // 컴포넌트가 언마운트될 때 Swapy 인스턴스 정리
    return () => {
      swapyRef.current?.destroy();
    };
  }, []);

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow ref={containerRef}>
            {columns.map((column, index) => (
              <TableCell 
                key={column.id} 
                className="swapy-slot" // Swapy 슬롯으로 지정
                data-swapy-slot={`slot-${column.id}`}
              >
                <div 
                  className="swapy-item" // Swapy 아이템으로 지정
                  data-swapy-item={`swapy-item-${column.id}`}
                >
                  {column.name}
                </div>
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              {columns.map((column) => (
                <TableCell key={column.id}>
                  {row[`col${column.id}`]}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
