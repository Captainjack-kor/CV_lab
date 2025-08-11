import React, { useState, useRef, useEffect } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';

const initialColumns = [
  { id: 'col1', header: '컬럼 1' },
  { id: 'col2', header: '컬럼 2' },
  { id: 'col3', header: '컬럼 3' },
];

const rows = [
  { id: 1, col1: '데이터 1', col2: '데이터 2', col3: '데이터 3' },
];

export default function DraggableTable() {
  const [columns, setColumns] = useState(initialColumns);
  const [draggedColumnIndex, setDraggedColumnIndex] = useState(null);
  const tableRef = useRef(null);

  const handleDragStart = (e, index) => {
    setDraggedColumnIndex(index);
    e.dataTransfer.setData('text/plain', index);
  };

  const handleDragOver = (e) => {
    e.preventDefault(); // 드롭 허용
  };

  const handleDrop = (e, targetIndex) => {
    e.preventDefault();
    const sourceIndex = parseInt(e.dataTransfer.getData('text/plain'), 10);
    const newColumns = [...columns];
    const [draggedColumn] = newColumns.splice(sourceIndex, 1);
    newColumns.splice(targetIndex, 0, draggedColumn);
    setColumns(newColumns);
    setDraggedColumnIndex(null);
  };

  return (
    <TableContainer component={Paper}>
      <Table ref={tableRef}>
        <TableHead>
          <TableRow>
            {columns.map((column, index) => (
              <TableCell
                key={column.id}
                draggable
                onDragStart={(e) => handleDragStart(e, index)}
                onDragOver={handleDragOver}
                onDrop={(e) => handleDrop(e, index)}
              >
                {column.header}
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
