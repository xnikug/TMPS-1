# SOLID Design Principles Report

## Author: Nicolae Marga, FAF-231

----

## Objectives:

* Implement at least 2 SOLID principles in a project;

## Used Design Principles: 

* **Single Responsibility Principle (S)**
* **Open/Closed Principle (O)**
* **Liskov Substitution Principle (L)**
* **Interface Segregation Principle (I)**
* **Dependency Inversion Principle (D)**

## Implementation

The implementation aims to contain all of the five SOLID principles in a task management system. The system separates concerns through classes, interfaces for extensibility, and makes use of dependency injection for loose coupling. Each class has a single responsibility, the system is open for extension but closed for modification, and dependencies are inverted through abstractions.

### Single Responsibility Principle (S)

Each class has one reason to change and one responsibility:

```php
// TaskReportGenerator - Only responsible for generating reports
class TaskReportGenerator {
    private TaskRepositoryInterface $repository;

    public function __construct(TaskRepositoryInterface $repository) {
        $this->repository = $repository;
    }

    public function generateStatusReport(): string {
        $tasks = $this->repository->findAll();
        $statusCounts = [];
        
        foreach ($tasks as $task) {
            $status = $task->status->value;
            $statusCounts[$status] = ($statusCounts[$status] ?? 0) + 1;
        }

        $report = "Task Status Report\n";
        $report .= "==================\n";
        foreach ($statusCounts as $status => $count) {
            $report .= ucfirst($status) . ": $count\n";
        }
        
        return $report;
    }
}
```

### Open/Closed Principle (O)

System is open for extension but closed for modification through interfaces:

```php
// NotificationService - Open for extension with new notifiers
class NotificationService {
    private array $notifiers = [];

    public function addNotifier(NotifierInterface $notifier): void {
        $this->notifiers[] = $notifier;
    }

    public function notifyAll(Task $task): void {
        foreach ($this->notifiers as $notifier) {
            $notifier->send($task);
        }
    }
}

// Easy to add new notification types without modifying existing code
class SmsNotifier implements NotifierInterface {
    public function send(Task $task): void {
        echo "SMS sent for task: {$task->title}\n";
    }
}

```

### Liskov Substitution Principle (L)

Derived classes can be substituted for their base classes:

```php
// All notifiers can be used interchangeably
interface NotifierInterface {
    public function send(Task $task): void;
}

// Any implementation can substitute the interface
$emailNotifier = new EmailNotifier();
$smsNotifier = new SmsNotifier('api-key');
$slackNotifier = new SlackNotifier('webhook-url');

// All can be used in the same context
function sendNotification(NotifierInterface $notifier, Task $task): void {
    $notifier->send($task);
}
```

### Interface Segregation Principle (I)

Interfaces are don't impose implementation of unused methods:

```php
// Simple, focused interface
interface NotifierInterface {
    public function send(Task $task): void;
}

// Repository interface with only necessary methods
interface TaskRepositoryInterface {
    public function save(Task $task): void;
    public function findById(int $id): ?Task;
    public function findAll(): array;
    public function findByStatus(TaskStatus $status): array;
    public function findOverdueTasks(): array;
}
```

### Dependency Inversion Principle (D)

High-level modules don't depend on low-level modules, both depend on abstractions:

```php
// TaskService depends on abstractions, not concrete classes
class TaskService {
    private NotifierInterface $notifier;
    private TaskRepositoryInterface $repository;

    public function __construct(NotifierInterface $notifier, TaskRepositoryInterface $repository) {
        $this->notifier = $notifier;
        $this->repository = $repository;
    }

    public function createTask(string $title, string $description, string $assignedTo = '', ?\DateTime $dueDate = null): Task {
        $task = new Task($title, $description, $assignedTo, $dueDate);
        $this->repository->save($task);
        
        if (!empty($assignedTo)) {
            $this->notifier->send($task);
        }
        
        return $task;
    }
}
```

### Complete Usage Example

```php
// Dependency injection in action
$repository = new InMemoryTaskRepository();
$emailNotifier = new EmailNotifier('smtp.example.com', 587);
$taskService = new TaskService($emailNotifier, $repository);

// Easy to swap implementations
$smsNotifier = new SmsNotifier('api-key-123');
$alternativeTaskService = new TaskService($smsNotifier, $repository);

// Multiple notifications
$notificationService = new NotificationService();
$notificationService->addNotifier($emailNotifier);
$notificationService->addNotifier($smsNotifier);
```

### Unit Tests Demonstrating SOLID Principles

```php
// Tests show loose coupling and substitutability
class TaskServiceTest extends TestCase {
    public function testCreateTaskWithNotification(): void {
        $mockNotifier = $this->createMock(NotifierInterface::class);
        $mockRepository = $this->createMock(TaskRepositoryInterface::class);
        $taskService = new TaskService($mockNotifier, $mockRepository);

        $mockNotifier->expects($this->once())
            ->method('send')
            ->with($this->isInstanceOf(Task::class));

        $task = $taskService->createTask('Test Task', 'Description', 'user@example.com');
        
        $this->assertEquals('Test Task', $task->title);
    }
}
```
**Test Results:**
- All unit tests pass with 100% coverage
- Mocking illustrates the dependency injection
- Each principle is validated through test cases
- System behavior is predictable and reliable
## Conclusions / Screenshots / Results

**Screenshots:**

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

The implementation effectively demonstrates all five SOLID principles within a practical task management system. 
Each class adheres to the **Single Responsibility Principle** by maintaining a clear and distinct purpose—for example, `TaskReportGenerator` focuses on generating reports, `NotificationService` handles notifications, and `TaskService` manages task-related operations. 
The system follows the **Open/Closed Principle** by allowing the addition of new notification types or repository implementations without altering existing code. Through the **Liskov Substitution Principle**, all notifier and repository implementations can be used interchangeably without disrupting system behavior. 
The **Interface Segregation Principle** is illustrated by defining interfaces such as `NotifierInterface` for sending notifications and `TaskRepositoryInterface` for storage-related operations. 
Lastly, the **Dependency Inversion Principle** is applied by ensuring that high-level modules rely on abstractions rather than concrete classes, allowing for greater flexibility through dependency injection.



