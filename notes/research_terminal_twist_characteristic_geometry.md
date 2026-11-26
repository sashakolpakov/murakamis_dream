# All-power terminal characteristics and their doubled normal channel

Private written proof, 16 November 2026.

This note classifies the classical terminal characteristic of every
fixed integer turn in the original operator algebra. It separates
the distinct reduced branches from their double algebraic
multiplicity. Both the intermediate spectral roots and the actual
physical shift roots stay separated on compact interior intervals.
No connection coefficient, finite-level transfer estimate, or
closed-source rate follows from this classification alone.

The complete-boundary charge characteristic and its two growing
modes were previously classified in
research_charge_characteristic_two_mode_block.md. That is a
different characteristic, with a varying charge and a complete
free boundary. Here the input is the original unit-turn operator
and its endpoint eigenvalue tending to \(2\). The cubic itself is
already present in the operator source below; the all-power
terminal parametrization, factorization, and multiplicity
classification are the assertions proved here.

## 1. The exact operator origin and the reduced terminal curve

Put \(N\ge2\), \(q=e^{\pi i/N}\),
\(P_N(Z)=2T_N(Z/2)+2\), \(c_0=q+q^{-1}\), and
\(\kappa=q^{(N-1)^2/2}\). Here \(T_N\) is the ordinary
Chebyshev polynomial; \(T\) and \(R\) below are the original
physical turn and crossing on \(\mathbb C[Z]/(P_N)\).
Use the operators
\[
 C f=Zf\pmod {P_N},\qquad J=TCT,\qquad
 V_n=\kappa^nTR^{-n}T,\qquad D_n=V_nCV_{-n},
 \qquad n\in\mathbb Z.
 \tag{1}
\]
The pinned operator source proves the exact quantum central
identity and the denominator-free recurrence for these operators,
including all physical first normals. Their commuting principal
symbols, denoted \(x,y,z\) for \(C,J,D_1\), satisfy
\[
 \mathcal F(x,y,z):=
 x^2+y^2+z^2+xyz-8(x+y+z)+28=0.
 \tag{2}
\]
The symbol \(x_n\) of \(D_n\) is the polynomial sequence
\[
 x_0=x,\qquad x_1=z,\qquad
 x_{k+2}=8-yx_{k+1}-x_k\quad(k\in\mathbb Z).
 \tag{3}
\]
The negative indices are defined by the same invertible recurrence.
Thus no division by a symbol or by a vanishing coefficient occurs.
These are formal leading symbols of the stated exact operators;
they are not a priori asymptotic descriptions of a source solution.

Define real polynomials
\[
 f_0(y)=2,\qquad f_1(y)=4-y,\qquad
 f_{k+1}(y)=8-yf_k(y)-f_{k-1}(y)\quad(k\ge1).
 \tag{4}
\]

**Theorem 1.** For \(n\ge1\), the reduced locus on (2) with
\(x_n=2\) is exactly
\[
             (x,y,z)=(f_n(y),y,f_{n-1}(y)).
 \tag{5}
\]
For \(n=-m\le-1\), it is exactly
\[
             (x,y,z)=(f_m(y),y,f_{m+1}(y)).
 \tag{6}
\]
In particular its equation in the \(x,y\) variables is
\(x=f_{|n|}(y)\). The condition for \(n=0\) is simply \(x=2\),
so it has no point over the physical interior \(-2<x<2\).

*Proof.* The transformation of an adjacent pair
\[
                (a,b)\longmapsto(b,8-yb-a)
\]
preserves \(\mathcal F(a,y,b)\): it is the exchange of the two
roots in the monic quadratic in \(a\), followed by swapping \(a,b\).
It is a polynomial automorphism, with inverse
\((a,b)\mapsto(8-ya-b,a)\).
At a terminal value \(b=2\), the cubic reduces exactly to
\[
                       \mathcal F(a,y,2)=(a+y-4)^2.
 \tag{7}
\]
On the reduced locus this forces the adjacent value \(4-y\).
Propagating backwards from \(x_n=2,x_{n-1}=4-y\) gives (5).
Propagating forwards from \(x_{-m}=2,x_{-m+1}=4-y\) gives (6).
Conversely each of these propagated sequences satisfies (2)
and the required terminal condition. \(\square\)

## 2. Explicit formula, real critical points, and endpoint values

Let \(T_k,U_k\) denote the ordinary Chebyshev polynomials of the
first and second kinds, and put \(U_{-1}=0\).

**Theorem 2.** For \(n\ge1\), \(f_n\) has degree \(n\), leading
coefficient \((-1)^n\), and the removable expression
\[
 f_n(y)=\frac{8+2(y-2)T_n(-y/2)}{y+2}.
 \tag{8}
\]
Its parity factorizations are
\[
 \begin{split}
 f_{2m}(y)-2
   &=[(y-2)U_{m-1}(-y/2)]^2,\qquad m\ge1,\\
 f_{2m+1}(y)-2
   &=(2-y)[U_m(-y/2)+U_{m-1}(-y/2)]^2,\qquad m\ge0.
 \end{split}
 \tag{9}
\]
Every critical point is real and simple. Every critical value
is at least \(2\). More explicitly:

* For \(n=2m\), put \(Q_m=(y-2)U_{m-1}(-y/2)\).
  The critical points are its \(m\) roots, of value \(2\),
  and the \(m-1\) strictly interlacing roots of \(Q_m'\),
  of value greater than \(2\).
* For \(n=2m+1\), put \(A_m=U_m(-y/2)+U_{m-1}(-y/2)\).
  The critical points are its \(m\) roots, of value \(2\),
  and one point in each interval between consecutive roots
  and between its last root and \(2\), of value greater than \(2\).
  When \(m=0\) there are no critical points.

The endpoint values are
\[
                 f_n(2)=2,\qquad f_n(-2)=2+4n^2.
 \tag{10}
\]
At level \(f_n=2\), all roots for even \(n\) are double.
For odd \(n\), the root \(y=2\) is simple and all other
roots are double. The point \(y=-2\) is never a critical point.

*Proof.* Away from \(y=-2\), subtract the fixed point
\(8/(y+2)\) from (4). The remaining recurrence has initial
values \(2(y-2)/(y+2)\) and
\((-y/2)\,2(y-2)/(y+2)\). The defining recurrence of \(T_n\)
gives (8). Since (4) is polynomial, the apparent singularity
is removable. The recurrence also gives its degree and leading
coefficient by induction.

Set \(v=-y/2\). The polynomial identities
\[
 T_{2m}(v)-1=2(v^2-1)U_{m-1}(v)^2,\qquad
 T_{2m+1}(v)-1=(v-1)[U_m(v)+U_{m-1}(v)]^2
 \tag{11}
\]
give (9) on substitution in (8). For example they follow
from \(T_k(\cos t)=\cos kt\) and
\(U_k(\cos t)=\sin((k+1)t)/\sin t\); equality on an interval
proves equality as polynomials.

The \(m\) roots of \(Q_m\) are \(2\) and
\[
              -2\cos(k\pi/m),\qquad 1\le k\le m-1.
 \tag{12}
\]
They are all simple, in \((-2,2]\). Rolle's theorem gives
one root of \(Q_m'\) in every consecutive interval, and its
degree \(m-1\) shows these are all its roots and all are simple.
They are disjoint from the roots of \(Q_m\).
Since \(f_{2m}'=2Q_mQ_m'\), this proves every assertion in
the even case, including simplicity of the critical points.

For odd degree the \(m\) roots of \(A_m\) are
\[
              -2\cos(2k\pi/(2m+1)),\qquad 1\le k\le m.
 \tag{13}
\]
Indeed
\[
 (U_m+U_{m-1})(\cos t)
       =\frac{\sin((2m+1)t/2)}{\sin(t/2)}.
 \tag{14}
\]
The listed roots are simple and lie in \((-2,2)\).
Differentiating (9) gives
\[
 f_{2m+1}'=A_m B_m,\qquad
 B_m=2(2-y)A_m'-A_m.
 \tag{15}
\]
For \(m\ge1\), \(B_m\) has degree \(m\).
Between consecutive roots of \(A_m\), and between its last
root and \(2\), the function \((2-y)A_m^2\) is positive
and has zero values at both ends. It therefore has an
interior critical point. These \(m\) points are roots of
\(B_m\). They exhaust its degree and are simple.
Also \(B_m(a)=2(2-a)A_m'(a)\ne0\) at any root \(a\) of \(A_m\).
Thus (15) has exactly the asserted simple roots. Their values
are \(2\) at the roots of \(A_m\) and strictly greater than
\(2\) at the others.

At \(y=2\), \(U_{m-1}(-1)=(-1)^{m-1}m\) and
\(A_m(2)=(-1)^m\). This proves the stated level-\(2\)
multiplicities; in the odd case \(f_{2m+1}'(2)=-1\).
At \(y=-2\), the recurrence is
\(f_{n+1}(-2)=8+2f_n(-2)-f_{n-1}(-2)\), with initial
values \(2,6\). This gives \(2+4n^2\).
All critical points just found lie strictly above \(-2\),
so that endpoint is not critical. \(\square\)

**Corollary 3.** For each fixed \(n\ne0\) and every real
\(x<2\), the equation \(f_{|n|}(y)=x\) has exactly \(|n|\)
distinct complex roots. For even \(|n|\) none is real.
For odd \(|n|\) exactly one is real; it lies above \(2\).
All the other roots occur in conjugate pairs.

The roots can be labeled holomorphically over
\(\mathbb C\setminus[2,\infty)\). In particular their separation
is uniform on every compact physical interval \(-2<x<2\).

*Proof.* Every critical value is on the omitted ray, so all
the roots in question are simple. The even polynomial is at
least \(2\) on the real line. In the odd case it is at least
\(2\) for \(y\le2\). For \(y>2\), all roots of \(A_m\) are
less than \(2\), and
\[
 \frac{A_m'(y)}{A_m(y)}
                    =\sum_{A_m(a)=0}\frac1{y-a}\ge0.
 \tag{16}
\]
Consequently \((y-2)A_m(y)^2\) increases strictly from zero
to infinity, also when \(m=0\). This gives the unique real
root and the remaining conjugate pairs.
The polynomial map is a proper unramified cover over
the simply connected slit domain
\(\mathbb C\setminus[2,\infty)\). Its \(|n|\) sheets therefore
give holomorphic root labels. Alternatively the local implicit
function theorem and continuation on this domain give the same
labels. Compactness gives the stated uniform separation.
\(\square\)

## 3. The terminal characteristic remains double

The reduced parametrization in Theorem 1 does not remove the
normal multiplicity of the original terminal condition.
Here is its exact algebraic form.

**Theorem 4.** Fix \(n\ne0\) and \(-2<x<2\). Every reduced
terminal point over \(x\) has multiplicity exactly two.
Its local coordinate algebra is the algebra of dual numbers.

*Proof.* For \(n\ge1\), use terminal coordinates
\[
             x_n=2,\qquad
             \delta=x_{n-1}+y-4.
 \tag{17}
\]
Equation (7) says exactly \(\delta^2=0\).
The inverse recurrence is linear in \(\delta\), and gives
\[
 \begin{split}
 x_0&=f_n(y)+\delta U_{n-1}(-y/2),\\
 x_1&=f_{n-1}(y)+\delta U_{n-2}(-y/2).
 \end{split}
 \tag{18}
\]
Indeed the coefficients of \(\delta\) start at \(0,1\)
and obey \(g_{k+1}=-yg_k-g_{k-1}\).
For \(n=-m\), take \(\delta=x_{-m+1}+y-4\); then
\[
 x_0=f_m(y)+\delta U_{m-1}(-y/2),\qquad
 x_1=f_{m+1}(y)+\delta U_m(-y/2).
 \tag{19}
\]

Put \(m=|n|\). All zeros of \(U_{m-1}(-y/2)\), if any,
are real and in \((-2,2)\), where \(f_m(y)\ge2\).
Thus this coefficient is a unit at every root of \(f_m(y)=x<2\).
After fixing \(x_0=x\), eliminate \(\delta\) from (18) or
(19). The local equation is precisely
\[
                         (f_m(y)-x)^2=0.
 \tag{20}
\]
Corollary 3 gives \(f_m'(y)\ne0\) there. Hence \(f_m(y)-x\)
is a local coordinate, and (20) is a double point with
coordinate algebra \(\mathbb C[\epsilon]/(\epsilon^2)\).
The polynomial automorphisms used in Theorem 1 preserve this
local algebra. \(\square\)

This is a statement about the classical terminal section,
not a removal of the finite-level normal equation. The actual
operator source retains the Jordan pair
\[
 (D_n-c_0)G_n=0,\qquad (D_n-c_0)H_n=G_n,
 \quad
 G_n=T(R^{-n}),\quad H_n=T(R^{-n}Q_N).
 \tag{21}
\]
Here \(Q_N=\left.\partial_wK_N(w,\cdot)\right|_{w=c_0}\)
uses the original kernel \(K_N\).
The classification does not identify their amplitudes or bound
the second one by the first. At \(x=2\), the unit coefficient
used to obtain (20) can vanish; the interior argument is not
extended to that boundary. The level-\(2\) polynomial
multiplicities in Theorem 2 remain exact there.

## 4. Physical shift roots and their separation

It is useful to check that separation of \(y\) branches is not
being substituted for separation of the physical shift roots.
Take a physical interior angle
\[
 x=2\cos\nu,\quad 0<\nu<\pi,\qquad
 a=\tan^2(\nu/2)=\frac{2-x}{2+x}>0.
 \tag{22}
\]
Let \(\tau\ne0\) denote the formal forward shift in the physical
row \(j\), with \(\nu=(2j+1)\pi/N\). This is a physical-value
chart, distinct from the Newton coefficient chart in the
operator source.
The physical symbols are
\[
 \boxed{\quad
 y=2+2a-a(\tau+\tau^{-1}),\qquad
 z=2+2a+a(e^{-i\nu}\tau+e^{i\nu}\tau^{-1}).
 \quad}
 \tag{23}
\]
For completeness, the exact physical formula in the source is
\[
 (Jp)(c(j))=c_0p(c(j))
      -A_j[p(c(j+1))-p(c(j))]
      -C_j[p(c(j-1))-p(c(j))],
 \tag{24}
\]
With \(s_h=2\sin(h\pi/N)\), its coefficients are
\[
 A_j=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\qquad
 C_j=\frac{s_j^4}{s_{2j}s_{2j+1}}.
\]
Both tend to \(a\) on an interior row. This gives \(y\).
To get \(z\), use the exact conjugation
\[
 D_1=\frac8{c_0}I+
                    \frac{q^{-1}JC-qCJ}{q^2-q^{-2}}.
 \tag{25}
\]
Writing \(\theta=\pi/N\), the forward coefficient is
\[
 -A_j\frac{q^{-1}c(j+1)-q c(j)}{q^2-q^{-2}}
       \longrightarrow a(\cos\nu-i\sin\nu).
 \tag{26}
\]
This follows from
\(c(j+1)-c(j)=-4\theta\sin\nu+O(\theta^2)\).
The backward coefficient is its conjugate. The diagonal
limit is
\(4-(1+a)x=2+2a\).
This proves (23) with the original shift convention; no
choice of a geometric branch was used.

**Theorem 5.** For every fixed \(n\ne0\) and \(-2<x<2\),
the physical characteristic \(x_n(x,y(\tau),z(\tau))=2\)
has exactly \(|n|\) distinct roots in \(\mathbb C^\times\),
each of multiplicity two. These distinct roots stay separated
and bounded away from zero and infinity on compact physical
intervals. None equals \(1\) or \(-1\).

*Proof.* The parametrization (23) identifies
\(\mathbb C^\times\) with the cubic slice \(\mathcal F(x,y,z)=0\).
To verify this and its injectivity explicitly, put
\(Y=y-(2+2a)\), \(Z=z-(2+2a)\), and temporarily replace
\(\tau,\tau^{-1}\) by independent \(t,s\).
The two linear equations in (23) have determinant
\(-2ia^2\sin\nu\ne0\), with inverse
\[
 t=-\frac{Z+e^{i\nu}Y}{2ia\sin\nu},\qquad
 s=\frac{Z+e^{-i\nu}Y}{2ia\sin\nu}.
 \tag{27}
\]
Direct substitution gives
\[
                  \mathcal F(x,y,z)
                       =4a^2\sin^2\nu\,(ts-1).
 \tag{28}
\]
Thus points of the cubic slice correspond exactly to \(ts=1\).
Theorem 1 and Corollary 3 give \(|n|\) distinct terminal
points, and Theorem 4 gives multiplicity two at each.
Their images under this nonsingular parametrization have the
same multiplicities and no other roots.

The only ramification values of \(\tau\mapsto y\) in (23)
are \(y=2\) at \(\tau=1\), and \(y=2+4a\) at \(\tau=-1\).
The first is impossible because \(f_m(2)=2>x\),
where \(m=|n|\). For even \(m\), no real \(y\) is a root.
For odd \(m\), the unique real root lies between \(2\)
and \(2+4a\). In fact \(A_{(m-1)/2}(2)^2=1\), and (16)
shows that its square is at least one for \(y>2\). Therefore
\[
 f_m(2+4a)\le2-4a
       <2-\frac{4a}{1+a}=x.
 \tag{29}
\]
Strict monotonicity above \(2\) gives the asserted location.
This excludes both ramification values, not merely a
collision in the intermediate \(y\) coordinate.
Continuity and compactness now give separation and the
nonzero finite bounds on compact intervals. \(\square\)

For odd \(|n|\), the physical shift belonging to the unique
real \(y\) branch is on the unit circle, since
\(2<y<2+4a\). For even \(|n|\) none of the terminal shifts
is on the unit circle: a unit-circle shift gives real \(y\),
which is excluded in that parity.
These statements do not order the moduli of the other shifts,
select a source solution, or establish Stokes control.
In particular the double roots remain double even though
the distinct roots are separated.

## 5. Direct-source readback and scope

The sole proof dependency was read completely in three
nontruncated parts, with the directly used identities and
its frozen hash checked:

* [Exact finite-band unit-turn operator and branching source](research_unit_turn_finite_band_branching_operator.md),
  SHA256
  31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  exact central relation (12d), all-integer recurrence (17a),
  original physical difference operator (21)--(22),
  and the retained Jordan companion (34)--(36).

The charge-characteristic note mentioned in the opening
coverage paragraph was also read completely. Its results
are not used in this proof.
All polynomial factorizations, critical-point counts,
physical-symbol limits, and local multiplicities used here
are proved above.
Only written mathematics, text reads and hashes were used.
No mathematical program, numerical experiment, test, or build
was run. Frozen notes and public manuscripts are unchanged.
