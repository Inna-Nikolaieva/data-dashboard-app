import { Typography, Box, TextField, IconButton } from '@mui/material';
import type { Comment } from '../../types/comment';
import { useAuth } from '../../hooks/useAuth.ts';
import { useComments } from '../../hooks/useComments.ts';
import { useState } from 'react';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import CheckIcon from '@mui/icons-material/Check';

interface Props {
  comment: Comment;
  onUpdate: (comment: Comment) => void;
  onDelete: (id: number) => void;
}

export default function CommentItem({ comment, onUpdate, onDelete }: Props) {
  const { user, isLoading } = useAuth();
  const { updateComment, deleteComment } = useComments();

  const [isEditing, setIsEditing] = useState(false);
  const [text, setText] = useState(comment.body);

  const canEdit = !isLoading && user?.id === comment.user.id;

  const handleSave = async () => {
    await updateComment({
      id: comment.id,
      data: { body: text },
    });

    onUpdate({
      ...comment,
      body: text,
    });

    setIsEditing(false);
  };

  const handleDelete = async () => {
    await deleteComment(comment.id);
    onDelete(comment.id);
  };

  return (
    <Box sx={{ mb: 1 }}>
      <Typography
        variant="body2"
        sx={{
          mt: 1,
          whiteSpace: 'pre-line',
        }}
      >
        @{comment.user.username}
      </Typography>

      {isEditing ? (
        <TextField
          size="small"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      ) : (
        <Typography
          variant="body2"
          sx={{
            mt: 1,
            color: 'text.secondary',
            whiteSpace: 'pre-line',
          }}
        >
          {comment.body}
        </Typography>
      )}

      {canEdit && (
        <Box>
          {isEditing ? (
            <IconButton onClick={handleSave}>
              <CheckIcon fontSize="small" />
            </IconButton>
          ) : (
            <IconButton onClick={() => setIsEditing(true)}>
              <EditIcon fontSize="small" />
            </IconButton>
          )}

          <IconButton onClick={handleDelete}>
            <DeleteIcon fontSize="small" />
          </IconButton>
        </Box>
      )}
    </Box>
  );
}
