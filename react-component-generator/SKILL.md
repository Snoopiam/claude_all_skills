---
name: react-component-generator
description: Scaffolds React components with TypeScript, hooks, and best practices. Use when user needs to create new React components, pages, or features.
---

# React Component Generator

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**Broken components are UNACCEPTABLE. Missing types are UNACCEPTABLE.**

### BANNED BEHAVIORS
```
NEVER say these after generating components:
❌ "I should have added proper types"
❌ "Let me fix that TypeScript error..."
❌ "I understand your frustration"
❌ "Upon compiling, there are type errors..."
❌ "I apologize for the broken component"

Do it right FIRST. Include all types and test mentally before delivering.
```

### SELF-INTERROGATION (Before submitting)
- [ ] Are all TypeScript types complete and correct?
- [ ] Does the component follow React best practices?
- [ ] Are props properly typed with defaults?
- [ ] Did I include accessibility attributes?

**If ANY answer is NO, keep working.**

---

You are an expert at creating well-structured React components with TypeScript.

## When to Use This Skill

- User needs a new React component
- User wants to scaffold a feature/page
- User needs component with specific patterns (forms, lists, modals)
- User wants TypeScript types for components

## Component Templates

### 1. Basic Functional Component

```tsx
import { FC } from 'react';

interface ComponentNameProps {
  title: string;
  className?: string;
}

export const ComponentName: FC<ComponentNameProps> = ({
  title,
  className = '',
}) => {
  return (
    <div className={`component-name ${className}`}>
      <h2>{title}</h2>
    </div>
  );
};
```

### 2. Component with State & Effects

```tsx
import { FC, useState, useEffect } from 'react';

interface DataItem {
  id: string;
  name: string;
}

interface ComponentNameProps {
  initialData?: DataItem[];
  onDataChange?: (data: DataItem[]) => void;
}

export const ComponentName: FC<ComponentNameProps> = ({
  initialData = [],
  onDataChange,
}) => {
  const [data, setData] = useState<DataItem[]>(initialData);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    onDataChange?.(data);
  }, [data, onDataChange]);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="component-name">
      {data.map((item) => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
};
```

### 3. Form Component

```tsx
import { FC, useState, FormEvent } from 'react';

interface FormData {
  email: string;
  password: string;
}

interface FormComponentProps {
  onSubmit: (data: FormData) => void | Promise<void>;
  isLoading?: boolean;
}

export const FormComponent: FC<FormComponentProps> = ({
  onSubmit,
  isLoading = false,
}) => {
  const [formData, setFormData] = useState<FormData>({
    email: '',
    password: '',
  });
  const [errors, setErrors] = useState<Partial<FormData>>({});

  const validate = (): boolean => {
    const newErrors: Partial<FormData> = {};

    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Invalid email format';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (validate()) {
      await onSubmit(formData);
    }
  };

  const handleChange = (field: keyof FormData, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    setErrors((prev) => ({ ...prev, [field]: undefined }));
  };

  return (
    <form onSubmit={handleSubmit} className="form-component">
      <div className="form-field">
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="email"
          value={formData.email}
          onChange={(e) => handleChange('email', e.target.value)}
          disabled={isLoading}
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>

      <div className="form-field">
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={formData.password}
          onChange={(e) => handleChange('password', e.target.value)}
          disabled={isLoading}
        />
        {errors.password && <span className="error">{errors.password}</span>}
      </div>

      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  );
};
```

### 4. List Component with Actions

```tsx
import { FC, useState } from 'react';

interface ListItem {
  id: string;
  title: string;
  description?: string;
}

interface ListComponentProps {
  items: ListItem[];
  onEdit?: (item: ListItem) => void;
  onDelete?: (id: string) => void;
  emptyMessage?: string;
}

export const ListComponent: FC<ListComponentProps> = ({
  items,
  onEdit,
  onDelete,
  emptyMessage = 'No items found',
}) => {
  const [selectedId, setSelectedId] = useState<string | null>(null);

  if (items.length === 0) {
    return <div className="list-empty">{emptyMessage}</div>;
  }

  return (
    <ul className="list-component">
      {items.map((item) => (
        <li
          key={item.id}
          className={`list-item ${selectedId === item.id ? 'selected' : ''}`}
          onClick={() => setSelectedId(item.id)}
        >
          <div className="list-item-content">
            <h3>{item.title}</h3>
            {item.description && <p>{item.description}</p>}
          </div>

          <div className="list-item-actions">
            {onEdit && (
              <button onClick={() => onEdit(item)}>Edit</button>
            )}
            {onDelete && (
              <button onClick={() => onDelete(item.id)}>Delete</button>
            )}
          </div>
        </li>
      ))}
    </ul>
  );
};
```

### 5. Modal Component

```tsx
import { FC, useEffect, useCallback, ReactNode } from 'react';
import { createPortal } from 'react-dom';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: ReactNode;
  closeOnOverlay?: boolean;
  closeOnEscape?: boolean;
}

export const Modal: FC<ModalProps> = ({
  isOpen,
  onClose,
  title,
  children,
  closeOnOverlay = true,
  closeOnEscape = true,
}) => {
  const handleEscape = useCallback(
    (e: KeyboardEvent) => {
      if (closeOnEscape && e.key === 'Escape') {
        onClose();
      }
    },
    [closeOnEscape, onClose]
  );

  useEffect(() => {
    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      document.body.style.overflow = 'hidden';
    }

    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = 'unset';
    };
  }, [isOpen, handleEscape]);

  if (!isOpen) return null;

  return createPortal(
    <div
      className="modal-overlay"
      onClick={closeOnOverlay ? onClose : undefined}
    >
      <div
        className="modal-content"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby={title ? 'modal-title' : undefined}
      >
        {title && (
          <div className="modal-header">
            <h2 id="modal-title">{title}</h2>
            <button
              className="modal-close"
              onClick={onClose}
              aria-label="Close modal"
            >
              ×
            </button>
          </div>
        )}
        <div className="modal-body">{children}</div>
      </div>
    </div>,
    document.body
  );
};
```

### 6. Custom Hook Template

```tsx
import { useState, useEffect, useCallback } from 'react';

interface UseApiOptions<T> {
  initialData?: T;
  autoFetch?: boolean;
}

interface UseApiReturn<T> {
  data: T | null;
  isLoading: boolean;
  error: Error | null;
  refetch: () => Promise<void>;
}

export function useApi<T>(
  fetchFn: () => Promise<T>,
  options: UseApiOptions<T> = {}
): UseApiReturn<T> {
  const { initialData = null, autoFetch = true } = options;

  const [data, setData] = useState<T | null>(initialData);
  const [isLoading, setIsLoading] = useState(autoFetch);
  const [error, setError] = useState<Error | null>(null);

  const fetch = useCallback(async () => {
    setIsLoading(true);
    setError(null);

    try {
      const result = await fetchFn();
      setData(result);
    } catch (err) {
      setError(err instanceof Error ? err : new Error('Unknown error'));
    } finally {
      setIsLoading(false);
    }
  }, [fetchFn]);

  useEffect(() => {
    if (autoFetch) {
      fetch();
    }
  }, [autoFetch, fetch]);

  return { data, isLoading, error, refetch: fetch };
}
```

## File Structure Convention

```
src/
├── components/
│   ├── common/           # Reusable components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── index.ts
│   │   └── Modal/
│   │       ├── Modal.tsx
│   │       └── index.ts
│   └── features/         # Feature-specific components
│       └── Stickers/
│           ├── StickerCard.tsx
│           ├── StickerGrid.tsx
│           └── index.ts
├── hooks/
│   ├── useApi.ts
│   └── useLocalStorage.ts
├── pages/
│   └── Home/
│       ├── Home.tsx
│       └── index.ts
└── types/
    └── index.ts
```

## Best Practices Checklist

```
□ Use TypeScript interfaces for props
□ Provide default values for optional props
□ Use semantic HTML elements
□ Add accessibility attributes (aria-*, role)
□ Handle loading and error states
□ Memoize callbacks with useCallback
□ Memoize expensive computations with useMemo
□ Clean up effects (return cleanup function)
□ Use key prop correctly in lists
□ Keep components focused (single responsibility)
```

## Process

1. **Ask** what component the user needs
2. **Clarify** requirements (props, state, behavior)
3. **Choose** appropriate template
4. **Generate** component with TypeScript
5. **Include** proper types, accessibility, error handling
6. **Suggest** file location in project structure
