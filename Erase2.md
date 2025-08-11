import React, { useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Menu,
  MenuItem,
} from '@mui/material';

export default function ContextMenuTable() {
  const [contextMenu, setContextMenu] = useState(null);

  const handleContextMenu = (event) => {
    event.preventDefault();
    setContextMenu(
      contextMenu === null
        ? {
            mouseX: event.clientX + 2,
            mouseY: event.clientY - 6,
          }
        : null,
    );
  };

  const handleClose = () => {
    setContextMenu(null);
  };

  return (
    <TableContainer component={Paper}>
      <Table onContextMenu={handleContextMenu}>
        <TableHead>
          <TableRow>
            <TableCell>컬럼 1</TableCell>
            <TableCell>컬럼 2</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {/* 예시 데이터 */}
          <TableRow>
            <TableCell>데이터 A</TableCell>
            <TableCell>데이터 B</TableCell>
          </TableRow>
          <TableRow>
            <TableCell>데이터 C</TableCell>
            <TableCell>데이터 D</TableCell>
          </TableRow>
        </TableBody>
      </Table>
      
      <Menu
        open={contextMenu !== null}
        onClose={handleClose}
        anchorReference="anchorPosition"
        anchorPosition={
          contextMenu !== null
            ? { top: contextMenu.mouseY, left: contextMenu.mouseX }
            : undefined
        }
      >
        <MenuItem onClick={handleClose}>옵션 1</MenuItem>
        <MenuItem onClick={handleClose}>옵션 2</MenuItem>
        <MenuItem onClick={handleClose}>옵션 3</MenuItem>
      </Menu>
    </TableContainer>
  );
}
