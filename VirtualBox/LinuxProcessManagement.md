
# Linux Process Management — Summary Notes

## 1. Process Monitoring

### `top`
- Real-time system monitor
- Displays CPU, memory, and running processes
- Basic and pre-installed

### `htop`
- Improved version of `top`
- Colorful and interactive UI
- Supports mouse and easier navigation
- Allows quick process control (kill, renice, etc.)
- Can display process tree

---

## 2. Process Identification

### UID (User ID)
- Identifies the **owner of a process**

### EUID (Effective User ID)
- Used by the system for **permission checks**

### GID / EGID
- Group equivalents of UID/EUID
- **EGID** determines group-level access permissions

---

## 3. Process States

Processes exist in different states:

- **Running (R)** → actively executing
- **Sleeping / Waiting (S)** → waiting for input/output or event
- **Stopped (T)** → paused by a signal
- **Zombie (Z)** → finished but still in process table (not yet cleaned up)

---

## 4. Process Signals (Inter-Process Communication)

Signals are used for **communication between processes** and system control.

### Common Signals

| Signal   | Number | Description |
|----------|--------|------------|
| SIGTERM  | 15     | Graceful termination |
| SIGKILL  | 9      | Forceful termination (cannot be ignored) |
| SIGSTOP  | —      | Pause process |
| SIGCONT  | —      | Resume process |

### Key Insight
- **SIGTERM (15)** → mild, allows cleanup
- **SIGKILL (9)** → brutal, immediate stop

---

## 5. Killing Processes

```bash
kill PID          # default SIGTERM (15)
kill -15 PID      # graceful stop
kill -9 PID       # force kill
````

In `htop`:

* Select process → press `F9` → choose signal

---

## 6. Finding Processes

```bash
ps aux
```

Filter specific processes:

```bash
ps aux | grep process_name
```

* Useful for locating running processes quickly

---

## 7. Process Priority (Niceness)

### Nice Value (NI)

* Range: **-20 to +19**

  * `-20` → highest priority
  * `0` → default
  * `+19` → lowest priority

### Commands

Start a process with a nice value:

```bash
nice -n 10 command
```

Change priority of a running process:

```bash
renice -n 10 -p PID
```

### Key Idea

* Higher nice value → lower priority (uses less CPU)
* Lower nice value → higher priority (uses more CPU)

---

## 8. `/proc` Filesystem

* Located at:

```bash
/proc
```

* A virtual filesystem exposing **live kernel data**

### Example

```bash
sudo cat /proc/PID/maps
```

* Shows memory mappings of a process
* May contain binary-like output

### Insight

* `/proc` is how the **kernel communicates process information to userspace**
* Includes:

  * Process state
  * Memory usage
  * Scheduling details

---

## 9. Kernel & Process Management

* The **kernel**:

  * Manages all processes
  * Allocates CPU time (scheduling)
  * Handles memory
  * Tracks process states

* Acts as the **core controller** of the system

---

## 10. Reading Manual Pages

```bash
man command_name
```

### Examples

```bash
man ps
man kill
```

### Navigation

* `q` → quit
* `/keyword` → search
* `n` → next result

---

## 11. File Type Checking

Check actual file type:

```bash
file filename
```

List files:

```bash
ls
ls -l
```

Extract extension:

```bash
echo "${filename##*.}"
```

---

## 12. Key Takeaways

* Processes are controlled by the **kernel**
* Signals enable **process communication and control**
* `SIGTERM (15)` = graceful, `SIGKILL (9)` = forceful
* `htop` simplifies monitoring and management
* `ps aux | grep` is essential for process lookup
* Niceness controls CPU scheduling priority
* `/proc` exposes real-time system and process data

---

## Next Step

* Study the **Linux File System**

```
```
