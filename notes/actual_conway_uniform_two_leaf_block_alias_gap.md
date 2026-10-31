# A uniform alias gap for an entire two-leaf Conway block

31 October 2026. This proof treats two leaves and
their original multiplication gate together. It holds on the entire
proper-seed range and removes the earlier individual-leaf condition
\(X\ge2/3\). Its finite certificate uses exact rational inequalities
with proved transcendental remainder bounds, not numerical sampling.

## 1. The original functions and the uniform statement

Retain the original complete, core and alias profiles

\[
\begin{gathered}
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 g(x)=J(2x)-4J(x),\\
 \widetilde g(x)=g(\max(x,1/4)),\quad 0\le x\le1/2,
 \qquad k(x)=-2J(x/2),\quad 0\le x\le1.
\end{gathered}                                                   \tag{1}
\]

The actual Newton product action and its whole domain are

\[
\begin{split}
 m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
        &\quad-J(z-x)-J(z-y)-J(x+y-z),\\
 D&=\{x,y\ge0:\ \max(x,y)\le z\le x+y\le1\}.
\end{split}                                                     \tag{2}
\]

All these actions are continuous and concave on their stated domains.
The tetrahedral decomposition of \(m\) proves this even when one input
exceeds \(1/2\). An alias is not assigned the support of a pure leaf.

At a complete optimized seed \(A_2\), set

\[
\begin{gathered}
 X=\cot(\pi a),\qquad \cot(\pi b)=X-\frac1{2X},\\
 F_2(b)=2g(a)+m(a,a,b),\qquad
 \lambda=F_2'(b)=2\log(2X^2).
\end{gathered}                                                   \tag{3}
\]

For \(1/2\le X\le1\) this state is strict, \(a\ge1/4\), and
\(-2\log2\le\lambda\le2\log2\). Define the dual upper envelopes

\[
\begin{split}
 Q_{AC}(\lambda)
   &=\max_{D,\ y\le1/2}
       [k(x)+\widetilde g(y)+m(x,y,z)-\lambda z],\\
 Q_{AA}(\lambda)
   &=\max_D[k(x)+k(y)+m(x,y,z)-\lambda z].
\end{split}                                                     \tag{4}
\]

**Uniform block lemma.** For every \(X\in[1/2,1]\),

\[
 Q_{AC}(\lambda),\ Q_{AA}(\lambda)
       \le F_2(b)-\lambda b-\frac1{100}.                         \tag{5}
\]

Equivalently, the corresponding output envelopes satisfy

\[
 G_{AC}(z),\ G_{AA}(z)
       \le F_2(b)+\lambda(z-b)-\frac1{100},\qquad 0\le z\le1.
                                                                    \tag{6}
\]

These are upper envelopes for the actual coefficients. No assertion
is made that a physical color or a signed coefficient attains them.
The coefficient bounds include the original normal terms, both level
parities and every retained half-twist sign, as checked in the
[exact block source proof](actual_conway_two_leaf_block_source_gap.md).

## 2. Reduction to finitely many global supporting inequalities

Let \(P(\lambda)\) be the maximum of
\(g(x)+g(y)+m(x,y,z)-\lambda z\) over \(D\) with both inputs at
most \(1/2\). At (3), both input derivatives vanish and the output
derivative is \(\lambda\). Concavity proves

\[
 P(\lambda)=F_2(b)-\lambda b.
                                                                    \tag{7}
\]

Explicitly, the original product derivatives at (3) are
\(m_x=m_y=-2\log X\) and \(m_z=2\log(2X^2)\), while
\(g'(a)=2\log X\). Thus the three derivatives of the pure dual
action vanish, including at the endpoints of the stated range.

Any strict rational pure state \(p=(a_p,a_p,b_p)\) gives the lower bound

\[
 P(\lambda)\ge A(p)-\lambda b_p,
       \qquad A(p)=2g(a_p)+m(p).                                  \tag{8}
\]

For either alias action \(H=k+\widetilde g+m\) or \(H=k+k+m\),
choose a rational strict state \(v\); for \(AC\), choose its core
coordinate above \(1/4\). The global tangent bound is

\[
 H(w)\le H(v)+\nabla H(v)\cdot(w-v).                              \tag{9}
\]

The full polytopes have exactly these vertices:

\[
\begin{split}
 V_{AC}={}&\{(0,0,0),(1,0,1),(1/2,1/2,1/2),
                     (0,1/2,1/2),(1/2,1/2,1)\},\\
 V_{AA}={}&\{(0,0,0),(1,0,1),(0,1,1),(1/2,1/2,1/2)\}.
\end{split}                                                      \tag{10}
\]

To check completeness, use nonnegative coordinates
\(p=z-x,q=z-y,r=x+y-z,w=1-x-y\), which obey
\(p+q+2r+w=1\). Thus \(D\) is a tetrahedron. Cutting it by
\(y\le1/2\) removes one vertex and adds the two displayed edge
intersections. A linear function attains its global maximum at a listed
vertex.

Partition \(\lambda/\log2\) into sixteen intervals

\[
 [-2+j/4,-2+(j+1)/4],\qquad j=0,\ldots,15.                       \tag{11}
\]

The [rational certificate table](../experiments/conway_two_leaf_block_alias_certificate.json)
specifies one pure state and one state for each alias action on each
interval, all with denominator \(10^6\). For every vertex \(w\) and
both endpoints \(t\) of its interval, the
[exact verifier](../experiments/verify_conway_two_leaf_block_alias_certificate.py)
checks

\[
 A(p)-t\log2\,b_p-H(v)-\nabla H(v)\cdot(w-v)
                        +t\log2\,w_z>\frac1{100}.                \tag{12}
\]

For each fixed vertex this expression is affine in \(t\), so its
endpoint checks cover the entire interval. Its dependence on \(w\)
is affine, so the vertex checks cover the entire polytope. Equations
(8)--(12) prove (5) for every real slope in the range. No assumption
about the location or uniqueness of an alias maximizer is used; core
plateau and boundary maximizers are included automatically.

There are 32 block comparisons and 288 endpoint/vertex inequalities.
Their smallest certified lower bound is

\[
 \frac{210002102902309638093785766005979344329}
      {5000000000000000000000000000000000000000}
           >\frac1{25}>\frac1{100}.                              \tag{13}
\]

The [result record](../experiments/conway_two_leaf_block_alias_certificate_results.json)
contains every rational lower bound. A candidate optimizer was useful
for finding the rational table; optimization is absent from verification
and is not a premise of the proof.

## 3. Rational enclosures for every transcendental expression

The verifier performs outward-rounded interval arithmetic with integer
endpoints at denominator \(10^{40}\). It uses no floating-point
trigonometric functions or special-function library. The gradients are

\[
\begin{split}
 g'(y)&=2\log\cot(\pi y),\qquad
 k'(x)=-\log(2\sin(\pi x/2)),\\
 m_x&=\log\frac{\sin\pi(x+y)\sin\pi(z-x)}
                    {\sin\pi x\sin\pi(x+y-z)},\\
 m_y&=\log\frac{\sin\pi(x+y)\sin\pi(z-y)}
                    {\sin\pi y\sin\pi(x+y-z)},\\
 m_z&=\log\frac{\sin\pi z\sin\pi(x+y-z)}
                    {\sin\pi(z-x)\sin\pi(z-y)}.
\end{split}                                                      \tag{14}
\]

All arguments are strictly positive at the rational states. For the
core derivative, cosine is evaluated as \(\sin\pi(1/2-y)\).

Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\), with
40 alternating terms and the next-term bound, encloses \(\pi\).
Reduce sine arguments to \((0,\pi/2]\), then use its Taylor polynomial
through degree 41 and the degree-43 remainder bound. Positive logarithm
arguments are rescaled by recorded powers of two. For
\(z=(x-1)/(x+1)\), the 80-term expansion

\[
 \log x=2\sum_{j=0}^{79}\frac{z^{2j+1}}{2j+1}+R,
       \qquad 0\le R\le\frac{2z^{161}}{161(1-z^2)}              \tag{15}
\]

is used on the explicitly checked interval \(0\le z<1/2\).
The same series at \(z=1/3\) encloses \(\log2\).

For the actions use \(J(0)=J(1/2)=J(1)=0\) and
\(J(1-t)=-J(t)\). Euler's sine product, followed by integration,
gives for \(0<t<1/2\)

\[
 J(t)=t\log(2\pi t)-t
          -\sum_{n=1}^{\infty}
               \frac{\zeta(2n)t^{2n+1}}{n(2n+1)}.               \tag{16}
\]

The expansion follows from \(\log(1-t^2/k^2)\); the remaining
integrated terms have one sign and are summable. The logarithmic term
is integrable at zero. Use \(\zeta(2)=\pi^2/6\), and for
\(2\le n\le20\) the rational integral-comparison bounds

\[
 \sum_{k=1}^{64}k^{-2n}\le\zeta(2n)
  \le\sum_{k=1}^{64}k^{-2n}+\frac{64^{1-2n}}{2n-1}.              \tag{17}
\]

Since \(\zeta(2n)<2\), the omitted part of (16) has absolute value
at most

\[
                    \frac{2t^{43}}{21\cdot43(1-t^2)}.           \tag{18}
\]

All inequalities in (12) therefore have proved rational enclosures.
Outward interval error can only weaken the certified gap. The verifier
checks feasibility, branch inequalities and contiguous slope coverage
as well as the final comparisons.

## 4. Consequence for the whole original source

The exact block source proof contracts only the two original leaves
and their one positive Newton multiplication gate. It retains
\(i+j\le N-1\), all phases and the full Hermite data. Internal first
derivatives vanish at the complete seed; its output derivative is
exactly (3). Using (6) therefore preserves every surrounding wire
derivative when the original stationary supporting planes are summed.

Every proper two-leaf seed in the retained \(C(FG)\), \(s\ge2\)
grammar has \(1/2<X<1\). Thus (5) applies automatically. Larger
proper seeds retain their old positive leaf margins. Every nonempty
alias sector loses a positive amount after summing the actual seed
and macro-product bounds. The \(d=N-1\) shifts cost only \(O(1)\)
in the exponent, and fixed trees have polynomially many wire states.

The all-core concave majorant and original far-color core estimate
then give the complete physical-color complement gap. The previously
primitive lattice, complex packet and marked geometry for
this entire grammar are unchanged. Consequently the original filling
transfer gives the hyperbolic knot complement volume after all
auxiliary fillings and a loop-free knot parity choice, without the
individual-leaf cutoff. Isolated \(C(A_2)\) is still excluded.

The old local-tangent example \(C(A_2\mathcal R(A_4))\) is now
covered: its negative individual deficit is compensated by the
original multiplication gate. The grammar still is not asserted to
represent every arborescent template.

## Verification and scope

The exact verification is reproducible with the standard Python library:

```sh
python experiments/verify_conway_two_leaf_block_alias_certificate.py
```

The separate [geometric response argument](actual_conway_two_leaf_monotone_alias_response.md) explains why the worst
conjugate gap occurs at the lower endpoint, but is not needed for this
proof: the finite certificate covers the whole interval directly.
