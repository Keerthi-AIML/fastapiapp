type Page = "home" | "chat" | "resume" | "jobmatch";

type Props = {
  onNavigate: (page: Page) => void;
};

function NavBar({ onNavigate }: Props) {
  const pages: Array<{ label: string; value: Page }> = [
    { label: "Home", value: "home" },
    { label: "Chat", value: "chat" },
    { label: "Resume", value: "resume" },
    { label: "Job Match", value: "jobmatch" },
  ];

  return (
    <nav style={{ display: "flex", gap: "1rem", padding: "1rem 2rem", borderBottom: "1px solid var(--border)", background: "var(--bg)" }}>
      {pages.map((page) => (
        <button key={page.value} type="button" onClick={() => onNavigate(page.value)}>
          {page.label}
        </button>
      ))}
    </nav>
  );
}

export default NavBar