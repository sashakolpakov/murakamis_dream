# The remaining small transform indices of the type-four source

Research deduction, 5 November 2026. After the already controlled
initial transform rows have been removed as complete sums, every
remaining row below the central transform interval can be transported
to its left face. The argument preserves the complete Newton sum.
Together with the private-tail and upper-triangle reductions, it leaves
a finite list of calibrated comparisons for the whole terminal
polynomial. Those comparisons are still hypotheses.

## 1. Source and order of the decomposition

Retain the exact square representation of
[the private-tail theorem](research_mixed_terminal_four_private_tails.md):
\[
 \mathcal V_{1,N}(w,X)=
 \sum_{i,j=0}^{N-1}
 \frac{X^{-i}p_i(X)}{P_i^2}
 \frac{p_j(r^i)\mathcal H_N(w,r^{-j})}{P_j^2}.
 \tag{1}
\]
Here \(r=e^{-2\pi i/N}\), \(P_i=(r;r)_i\),
\(p_i(X)=(rX;r)_i\), \(X=e^{-2\pi ia}\), and
\(a=y+iH\in[.22,.45]+i[-.12,.12]\).
The products in (1) vanish exactly when \(i+j\ge N\).
The factor \(\mathcal H_N\) is the whole ordinary endpoint
polynomial, including all of its Newton indices and derivatives.

First remove all outer rows with \(i/N\le\delta\), for a
sufficiently small fixed \(\delta>0\). These rows include their
whole private and Newton sums. The previously proved
[terminal end-tail bound](research_mixed_terminal_transform_tails.md)
gives them a strict gap below the bare terminal supporting plane.
This step does not license restricting either inner sum afterward.

For the remaining small transform indices put
\[
       t=i/N\in[\delta,.15],\qquad e=j/N\in[0,1].
 \tag{2}
\]
We split only this part of the source according to whether \(e\)
lies below, inside, or above \([.27,.49]\). Rounding the
splitting points to physical indices is handled at the end.

## 2. The central private indices and their exact contours

On
\[
 E_c=[.27,.49]+i[-.055,.04]
 \tag{3}
\]
the complete endpoint interpolation has its proved holomorphic packet.
The exact two-index interpolation, before taking any asymptotic
approximation, is that of
[the reduced-current theorem](research_mixed_terminal_four_reduced_currents.md).
Its phase is
\[
\begin{split}
 \Phi_1(a;e,t)={}&S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)\\
             &-i\pi(e-e^2)/2+2\pi iat,\qquad
 g(z)=J(z)+i\pi(z-z^2)/2.
\end{split}
 \tag{4}
\]
For real \(t\) as in (2), all its factorial arguments remain
in the original regular strips. No endpoint packet is being
continued beyond (3).

**Lemma 1.** On (2)--(3),
\[
                 \partial_t\Re\Phi_1(a;e,t)>\log(13/10).
 \tag{5}
\]

*Proof.* Write \(h=\Im e\). Differentiating the original
phase, including its quadratic marks, gives
\[
 \partial_t\Re\Phi_1
 =\log\frac{|2\sin\pi(a+t)|\,|2\sin\pi(e+t)|}
                  {(2\sin\pi t)^3}+\pi(h-H).
 \tag{6}
\]
The real shifted intervals are \([.22,.60]\) and
\([.27,.64]\). On these intervals the sine is respectively
greater than \(63/100\) and \(74/100\). Also
\(\sin(.15\pi)<23/50\) and
\(e^{.175\pi}<9/5\). Imaginary parts can only increase
the modulus of a sine. Since \(h-H\ge-.175\), (6) gives
\[
 \exp(\partial_t\Re\Phi_1)
 >\frac{(126/100)(148/100)}{(92/100)^3}\frac59
 >\frac{13}{10}.
 \tag{7}
\]
All bounds are elementary scalar inequalities. For explicit rational
checks, use the lower sine polynomial \(x-x^3/6\) at
\(.22(3.14)\) and \(.27(3.14)\), and at the reflected
upper endpoints \(.40(3.14)\), \(.36(3.14)\).
For the upper sine bound use
\(x-x^3/6+x^5/120\) at \(x=.15(22/7)\).
Finally \(.175\pi<11/20\), and the exponential series
through degree four with its geometric tail bound gives
\[
 e^{11/20}\le
 \sum_{k=0}^{4}\frac{(11/20)^k}{k!}
 +\frac{(11/20)^5}{5!(1-(11/20)/6)}<9/5.
\]
This proves (5). \(\square\)

Consequently every such phase value is bounded by its value at
\(t=.15\), minus \(\log(13/10)(.15-t)\).
For each fixed physical \(i\) in (2), apply the exact residue
formula only in the private index. It gives one shifted horizontal
integral at the actual private critical height, two joins, two
horizontal aliases at heights \(-.055,.04\), and the vertical
alias sides. First apply (5) to each point of each current. The
private-index residue penalty is unchanged by this operation.
At the resulting face \(t=.15\), vertical convexity is supplied
by the reduced-current Hessian theorem. It bounds the joins and
vertical aliases by their real and horizontal endpoints.

Thus precisely the following already listed current comparisons
control this whole part of (2): the flattened \(t=.15\) face,
the two real corners \((t,e)=(.15,.27),(.15,.49)\), and
the private-index aliases with transform height zero. No additional
face family is required. Convexity has only been used after transport
to the domain where it is proved.

## 3. The two real corner regions

Let \(\lambda(e)=\Re S(e)\), with continuous endpoint values
zero, and retain the exact external rate
\[
 Q_a(t)=\int_0^t
       \log|e^{-2\pi H}-e^{-2\pi i(y+s)}|\,ds.
 \tag{8}
\]
For physical \(t\), the uniform envelope for the whole
\(\mathcal H_N\) in the private-tail theorem gives the rate
\[
 \mathcal R(a;t,e)=Q_a(t)-2J(t)
                  +\lambda(e)-J(e)+I_t(e),
 \quad I_t(e)=\int_0^e\log|1-e^{-2\pi i(t+s)}|\,ds.
 \tag{9}
\]
This bounds the modulus after summing the Newton index completely.
It is uniform through \(e=0,1\); compact-index asymptotics alone
would not justify this statement.

For \(0\le e\le.27\) and (2), one has
\(e+t\le.42\), so \(I_t(e)=J(e+t)-J(t)\).
Differentiation in \(t\) gives
\[
 \exp(\mathcal R_t)
 =e^{-\pi H}
   \frac{|\sin\pi(a+t)|\sin\pi(e+t)}{2\sin^3\pi t}
 \ge e^{-.12\pi}
             \frac{\sin\pi(y+t)}{2\sin^2\pi t}.
 \tag{10}
\]
The inequality uses \(t\le e+t<1/2\). For each fixed \(y\),
the last sine quotient decreases with \(t\) on \((0,.15]\),
since its logarithmic derivative is
\(\pi\cot\pi(y+t)-2\pi\cot\pi t<0\).
At \(t=.15\), the numerator exceeds \(9/10\), the
denominator is less than \(2(23/50)^2\), and
\(e^{-.12\pi}>2/3\). Therefore
\[
                \mathcal R_t>\log(7/5).
 \tag{11}
\]
For the numerator use the lower sine polynomial on the endpoint
angles \(.37\pi,.60\pi\); symmetry reduces the latter to
\(.40\pi\). The exponential inequality follows by the same
positive-series bound as in Lemma 1, with \(.12\pi<19/50\).

Transport first to \(t=.15\). The lower private-tail estimate
then transports \(e\) to \(.27\). Its anchor equality with
the original phase gives
\[
 \mathcal R(a;t,e)
 \le\Re\Phi_1(a;.27,.15)
       -\log(7/5)(.15-t)-\frac{13}{100}(.27-e).
 \tag{12}
\]

For \(e\ge.49\), keep \(t\) fixed and real. The derivative
of \(\lambda(e)-J(e)+I_t(e)\) in \(e\) is less than
\(-1/2\). On \([.49,.5]\), this follows from
\(\lambda'<-3/5\), \(J'>3/5\), and
\(\log|1-e^{-2\pi i(t+e)}|\le\log2<7/10\).
Above \(.5\), use \(\lambda'-J'\le-\log4\).
These estimates hold for every real \(t\), including across
the logarithmic zero after integration. Transport \(e\) to
\(.49\), then apply Lemma 1 at that real private cut. The result is
\[
 \mathcal R(a;t,e)
 \le\Re\Phi_1(a;.49,.15)
       -\log(13/10)(.15-t)-\tfrac12(e-.49).
 \tag{13}
\]
The physical terms beyond \(i+j=N\) remain exactly zero.
The continuous rate used to establish (13) does not revive them.

Equations (12)--(13) control the positive majorant of these two
corner regions, with the Newton sum kept whole within each row.
Thus they require only the two left real-corner comparisons already
present in the reduced-current criterion.

## 4. Finite-source conclusion and the exact remaining comparisons

**Proposition 2.** Suppose the left flattened face, the two left
real corners, and the two private-alias families at transform height
zero have a common strict gap below the bare terminal supporting
plane, as required in the reduced-current criterion. Then the entire
part (2) of the original finite sum has a strict gap below that plane.
The assertion holds on a sufficiently small fixed ordinary-color
disk, for both parities and every fixed ordinary-color derivative.

*Proof.* For central private indices, use the exact one-index residue
argument following Lemma 1 and the uniform complete-endpoint packet
on (3). For the other private indices, use (9), (12) and (13).
All these finite estimates permit an arbitrarily small common
positive rate tolerance. The number of physical rows, residue
factors, and contour lengths costs polynomial factors. Choose the
tolerance smaller than the assumed strict gap. Cauchy's formula
on a smaller fixed color disk handles every fixed derivative.

Choose the integer splitting indices first and place each contour
cut halfway between successive indices. Any discrepancy from
\(.15,.27,.49\) is \(O(N^{-1})\). After transport to
the regular anchor faces, all phase derivatives are uniformly bounded,
and the assumed strict inequalities persist on a fixed neighborhood.
Thus the rounding costs \(O(N^{-1})\) in rate and does not omit
a physical row. This proves the proposition. \(\square\)

There is now a finite sufficient list for the complete type-four
terminal theorem:

1. The eight flattened comparisons and twelve alias families of
   the reduced-current criterion.
2. The single raw half-period comparison of
   [the upper-triangle reduction](research_mixed_terminal_four_right_triangle.md).

To see that no physical region is missing, first remove the complete
coherent rows \(i/N\le\delta\). For
\(\delta<i/N<.15\), use Proposition 2. For
\(.15\le i/N<.5\), the central private strip is the reduced
rectangle and both private complements are the two private-tail
sectors. For \(i/N\ge.5\), use the upper-triangle theorem.
At the upper central cut choose the half-grid line just above the
largest physical index strictly less than \(N/2\). This is
\(.5\) at odd levels and \(.5-1/(2N)\) at even levels.
The even row \(i=N/2\) belongs to the upper triangle.
The private and lower transform cuts are matched in the same way.
This is a disjoint finite partition of (1).

If all twenty-one comparisons pass uniformly on the original
reference families, the retained rectangle supplies the nonzero
\(N^{-2}\) geometric term and every complementary part just
listed is exponentially smaller. It would follow that the whole
\(\mathcal V_{1,N}\) has that term and the required external
supporting-plane bound. The twenty-one signs have not been proved
in this note, so this consequence remains conditional. No conclusion
about the full knot invariant follows from the reduction alone.
