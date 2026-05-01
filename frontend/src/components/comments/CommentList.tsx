import { Box } from '@mui/material';
import CommentItem from './CommentItem';
import type { Comment } from '../../types/comment';
import { useState } from 'react';

interface Props {
  initialComments: Comment[];
}

export default function CommentList({ initialComments }: Props) {
  const [comments, setComments] = useState<Comment[]>(initialComments);

  const handleUpdate = (updated: Comment) => {
    setComments((prev) =>
      prev.map((c) => (c.id === updated.id ? { ...c, body: updated.body } : c))
    );
  };

  const handleDelete = (id: number) => {
    setComments((prev) => prev.filter((c) => c.id !== id));
  };

  return (
    <Box sx={{ mt: 2, pl: 2, borderLeft: '2px solid #eee' }}>
      {comments.map((c) => (
        <CommentItem
          key={c.id}
          comment={c}
          onUpdate={handleUpdate}
          onDelete={handleDelete}
        />
      ))}
    </Box>
  );
}
