import { useState } from 'react';
import {
  Card,
  CardContent,
  Typography,
  IconButton,
  Collapse,
  Button,
  Box,
  Divider,
} from '@mui/material';

import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';

import { useAuth } from '../../hooks/useAuth.ts';
import type { Post } from '../../types/post';
import CommentList from '../comments/CommentList';

interface Props {
  post: Post;
  onEdit: (post: Post) => void;
  onDelete: (id: number) => void;
}

export default function PostCard({ post, onEdit, onDelete }: Props) {
  const [showComments, setShowComments] = useState<boolean>(false);
  const { user, isLoading } = useAuth();

  const canEdit = !isLoading && user?.id === post.user.id;

  return (
    <Card
      sx={{
        mb: 2,
        borderRadius: 3,
        boxShadow: '0 2px 10px rgba(0,0,0,0.08)',
      }}
    >
      <CardContent>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <Typography variant="h6" sx={{ fontWeight: 600 }}>
            {post.title}
          </Typography>

          {canEdit && (
            <>
              <IconButton onClick={() => onEdit(post)}>
                <EditIcon fontSize="small" />
              </IconButton>

              <IconButton onClick={() => onDelete(post.id)}>
                <DeleteIcon fontSize="small" />
              </IconButton>
            </>
          )}
        </Box>

        <Typography
          variant="body2"
          sx={{
            mt: 1,
            color: 'text.secondary',
            whiteSpace: 'pre-line',
          }}
        >
          {post.body}
        </Typography>

        <Typography
          variant="caption"
          sx={{ display: 'block', mt: 1, color: 'gray' }}
        >
          Posted by @{post.user.username}
        </Typography>

        <Divider sx={{ my: 1.5 }} />

        <Button
          size="small"
          onClick={() => setShowComments((prev) => !prev)}
          startIcon={showComments ? <ExpandLessIcon /> : <ExpandMoreIcon />}
        >
          {showComments
            ? 'Hide comments'
            : `Show comments (${post.comments?.length ?? 0})`}
        </Button>

        <Collapse in={showComments} timeout="auto" unmountOnExit>
          <Box sx={{ mt: 2 }}>
            <CommentList initialComments={post.comments} />
          </Box>
        </Collapse>
      </CardContent>
    </Card>
  );
}
