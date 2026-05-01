import { Stack, TextField, Button } from '@mui/material';
import { useState, useEffect } from 'react';

type PostFormValues = {
  title: string;
  body: string;
};

interface Props {
  initialValues: Partial<PostFormValues>;
  onSubmit: (data: PostFormValues) => void | Promise<void>;
}

export function PostForm({ initialValues, onSubmit }: Props) {
  const [form, setForm] = useState<PostFormValues>({
    title: '',
    body: '',
    ...initialValues,
  });

  useEffect(() => {
    setForm((prev) => ({
      ...prev,
      ...initialValues,
    }));
  }, [initialValues]);

  return (
    <Stack spacing={2}>
      <TextField
        label="Title"
        value={form.title}
        onChange={(e) =>
          setForm((prev) => ({
            ...prev,
            title: e.target.value,
          }))
        }
      />

      <TextField
        label="Body"
        value={form.body}
        onChange={(e) =>
          setForm((prev) => ({
            ...prev,
            body: e.target.value,
          }))
        }
      />

      <Button variant="contained" onClick={() => onSubmit(form)}>
        Save
      </Button>
    </Stack>
  );
}
