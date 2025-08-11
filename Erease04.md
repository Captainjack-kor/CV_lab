import React, { useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';
import DragIndicatorIcon from '@mui/icons-material/DragIndicator';

const initialColumns = [
  { id: 'col1', header: '컬럼 1' },
  { id: 'col2', header: '컬럼 2' },
  { id: 'col3', header: '컬럼 3' },
];

const rows = [
  { id: 1, col1: '데이터 1', col2: '데이터 2', col3: '데이터 3' },
  { id: 2, col1: '데이터 4', col2: '데이터 5', col3: '데이터 6' },
];

export default function DraggableTable() {
  const [columns, setColumns] = useState(initialColumns);

  const handleDragStart = (e, index) => {
    // 드래그 시작 시 인덱스 저장
    e.dataTransfer.setData('text/plain', index.toString());
  };

  const handleDragOver = (e) => {
    // 드롭 가능하도록 기본 동작 방지
    e.preventDefault();
  };

  const handleDrop = (e, targetIndex) => {
    // 드롭 시 컬럼 순서 변경
    e.preventDefault();
    const sourceIndex = parseInt(e.dataTransfer.getData('text/plain'), 10);

    // 같은 위치에 드롭하는 경우
    if (sourceIndex === targetIndex) {
      return;
    }

    const newColumns = [...columns];
    const [draggedColumn] = newColumns.splice(sourceIndex, 1);
    newColumns.splice(targetIndex, 0, draggedColumn);
    setColumns(newColumns);
  };

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            {columns.map((column, index) => (
              <TableCell
                key={column.id}
                onDragOver={handleDragOver}
                onDrop={(e) => handleDrop(e, index)}
              >
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <DragIndicatorIcon
                    style={{ cursor: 'grab' }}
                    draggable
                    onDragStart={(e) => handleDragStart(e, index)}
                  />
                  <span>{column.header}</span>
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
                  {row[column.id]}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
