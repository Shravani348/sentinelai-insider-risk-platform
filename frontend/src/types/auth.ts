// frontend/src/types/auth.ts
export interface User {
  id: number;
  employee_id: string;
  email: string;
  full_name: string;
  role: 'Admin' | 'Manager' | 'Employee';
  department: string;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}