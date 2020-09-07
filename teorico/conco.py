import rx
import rx.operators as ops

#source = rx.from_iterable([1, 2, 3, 4, 5])
source = rx.from_iterable([5, 4, 3, '2', 1])


disposable = source.pipe(
    # ops.map(lambda i: i - 1),
    ops.filter(lambda i: i % 2 == 0)
).subscribe(
    on_next=lambda i: print(f'on next: {i}'),
    on_completed=lambda: print('on completed:'),
    on_error=lambda e: print(f'on error: {e}')
)

disposable.dispose()

print('fim')
