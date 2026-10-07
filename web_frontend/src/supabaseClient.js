import { createClient } from "@supabase/supabase-js";

const supabaseUrl = "https://albxlanqtdbvvhowwrgi.supabase.co";
const supabaseAnonKey = "sb_publishable_SSe6liTsfBwO8I7SUbETJA__HUY64lb";

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
