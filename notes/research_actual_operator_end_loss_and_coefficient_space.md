# Classical end loss and coefficient-space reduction for the actual operator

Research note, 6 November 2026. Two exact reductions apply to the
primitive minimal normal operator of every actual fixed knot.
Its two classical end losses agree by the original Weyl symmetry,
and no finite exact left-multiple annihilator removes either loss.
Independently, its finite Laurent-polynomial solution space has a
dimension bound independent of the level, even when end loss occurs.

These facts do not prove the end condition of the
[microscopic-disk theorem](research_regularized_microscopic_disk_growth.md),
nor a quantitative observation bound from a finite jet block.
A formal \(H\)-adic reduction is possible, but its discarded
remainder still contains the whole actual source.

## 1. The fixed actual equation

Use the exact conventions of
[actual Weyl descent, Sections 2–3](actual_weyl_descent.md):
\[
 q_N=e^{\pi i/N},\qquad Q_N=q_N^2,\qquad
 T_N f(Y)=f(Q_NY),\qquad v_N=(Y-1)F_N.
 \tag{1}
\]
Let \(\mathcal K=\mathbb C(q,Y)\), with
\(\sigma f(q,Y)=f(q,q^2Y)\). The all-level annihilator ideal of
the original \(v_N\), with finitely many exceptional levels
permitted, is a nonzero left ideal in
\(\mathcal K[T^{\pm1};\sigma]\). Its primitive minimal generator
can be written
\[
 B=\sum_{i=0}^{d}b_i(q,Y)T^i,\qquad
 b_i\in\mathbb C[q^{\pm1},Y^{\pm1}],\quad
 \gcd_i b_i=1,\quad b_0b_d\ne0.
 \tag{2}
\]
The actual finite-array construction proves existence; it does
not supply an efficient formula for arbitrary knots. Its
coefficient primitivity implies
\[
 B_{\rm cl}(Y,L)=\sum_i b_i(1,Y)L^i\ne0.
 \tag{3}
\]
The question is whether the two ends in (3) remain nonzero
as polynomials in \(Y\), not whether they are nonzero at \(Y=1\).

The original regularized source is
\[
 F_N=S_NR_N+P_N,\qquad
 S_N=\frac{Y^N-1}{Y-1},\qquad
 B(q_N,Y,T_N)R_N=\beta_N=-B(q_N,Y,T_N)\frac{P_N}{S_N}.
 \tag{4}
\]
Here \(R_N\) is Laurent polynomial with support in
\([-AN,AN]\) for a fixed integer \(A\). The complete combination
\(\beta_N\) is Laurent polynomial on fixed support with
polynomially bounded coefficients. All quotient-root poles
cancel in that complete combination. These are the actual
identities and bounds of
[growth characteristics, Sections 1–2](research_regularized_period_growth_characteristics.md);
none of the individual shifted polar terms is discarded.

## 2. End losses are additive under exact multiplication

For a nonzero finite Laurent Ore operator
\(D=\sum_{i=a}^{b}d_i(q,Y)T^i\), define
\[
 \begin{split}
 \nu(D)&=\min_i\operatorname{ord}_{q-1}d_i,\\
 D^\circ(Y,L)&=\left.(q-1)^{-\nu(D)}D\right|_{q=1},\\
 a^\circ&=\min\operatorname{supp}_L D^\circ,\qquad
 b^\circ=\max\operatorname{supp}_L D^\circ,\\
 \ell_-(D)&=a^\circ-a,\qquad
 \ell_+(D)=b-b^\circ .
 \end{split}
 \tag{5}
\]
Valuations are taken over the coefficient field \(\mathbb C(Y)\);
thus rational coefficient representatives are allowed. Both losses
are nonnegative integers.

**Proposition 1.** For any two nonzero finite operators \(C,D\),
\[
 \nu(CD)=\nu(C)+\nu(D),\qquad
 (CD)^\circ=C^\circ D^\circ,\qquad
 \ell_\pm(CD)=\ell_\pm(C)+\ell_\pm(D).
 \tag{6}
\]
The product in the middle formula is commutative.

Indeed \(\sigma^i\) preserves \(q-1\) valuation and reduces to the
identity on \(\mathbb C(Y)\). The candidate initial product is
therefore \(C^\circ D^\circ\), which is nonzero in the integral
domain \(\mathbb C(Y)[L^{\pm1}]\). This proves the first two
claims. The extreme quantum coefficients are nonzero products,
so the quantum support endpoints add too. The two classical
support endpoints add in the same integral domain. Subtraction
proves the last assertion.

A nonzero rational scalar, on either side, has both losses zero.
So does a Laurent shift \(T^k\). Consequently clearing
coefficient denominators, removing common scalar content,
and changing the starting shift index do not alter the losses.
These operations must of course still be recorded when
specializing an actual equation.

**Corollary 2.** Every nonzero finite exact annihilator \(D\)
of the same actual normal-state family is a left multiple
\(D=CB\) in the localized Ore ring. Thus
\[
                         \ell_\pm(D)\ge\ell_\pm(B).
 \tag{7}
\]
In particular, if the primitive minimal \(B\) loses either
classical end, no finite exact left-multiple construction,
including primitive scalar renormalization, produces an
annihilator of that family with both ends preserved.

This statement is specifically about the homogeneous original
normal-state ideal. It does not exclude a different affine
equation for \(R_N\) with a separately controlled source that
does not arise from an annihilator of \(v_N\). Equation (4)
alone does not identify every possible affine-source ideal.

## 3. The original Weyl symmetry pairs the losses

The exact primitive reciprocity proved in the Weyl note has
the coefficient form
\[
 b_{d-i}(q,Y)
   =h(q,Y)\,q^{2i}
       b_i(q,q^{-2d}Y^{-1}),
 \tag{8}
\]
where \(h\) is its specified nonzero Laurent monomial unit.
The substitution in (8) preserves \(q-1\) valuation, so
\[
 \operatorname{ord}_{q-1}b_i
       =\operatorname{ord}_{q-1}b_{d-i}.
 \tag{9}
\]
Since \(\nu(B)=0\), there is an integer
\(0\le r\le\lfloor d/2\rfloor\) such that
\[
 B_{\rm cl}(Y,L)=L^r C(Y,L),\qquad
 C(Y,0)\ne0,\quad \deg_L C=d-2r,\qquad
 \ell_-(B)=\ell_+(B)=r.
 \tag{10}
\]
Thus the missing microscopic-disk end condition is exactly
\(r=0\). Weyl symmetry reduces it to one condition but does not
set \(r\) to zero. In particular a nonzero order-one primitive
operator automatically has \(r=0\); a higher-order primitive
operator can have a nonzero middle classical coefficient while
both ends have positive \(q-1\) valuation.

There is an additional actual-source implication when
\(d-2r=0\). In that case the classical characteristic is a
single nonzero monomial \(c(Y)L^r\). The positive joint growth
envelope of the actual \(R_N\) is then identically zero.
To see this, off the finite zero set of \(c\), any finite
positive envelope point would supply nearby positive
first-order upper contacts by quadratic penalization. The
[whole-source characteristic theorem](research_regularized_period_growth_characteristics.md)
would require \(c(Y)e^{2\pi i r p}=0\), which is impossible.
The finite nonnegative subharmonic envelope
\(V=\max(U,0)\) is therefore zero off that finite set, and its
submean inequality makes it zero there too.

Hence a proved positive complete-value limsup for an actual
knot rules out a monomial classical symbol for its primitive
normal operator. In particular, for a knot with such positive
growth and \(d\le2\), the end condition follows. This does not
assume or prove positive complete growth for arbitrary knots.
The relation \(NR_N(1)=K_N-P_N(1)\), with polynomially bounded
\(P_N(1)\), is the original reason complete positive growth
implies positive joint growth.

## 4. Formal reduction is possible, but is not a new finite recurrence

Put \(H=\log Q\). Work over
\(\mathbb C(Y)[[H]]\), with
\(\sigma f(Y)=f(e^H Y)\), allowing finite Laurent \(T\)-support
at each \(H\)-coefficient. Normalize the monic polynomial part
of (10) as \(C_0(L)\). There is a formal factorization
\[
 B=U\,\widehat C,\qquad
 \widehat C=C_0+\sum_{n\ge1}H^n C_n,\quad
 \deg_T C_n<e:=d-2r,\qquad
 U_0=a(Y)T^r ,
 \tag{11}
\]
with \(\widehat C\) monic of fixed degree \(e\). The leading
coefficient \(a(Y)\) is nonzero. If \(e=0\), take
\(\widehat C=1\) and \(U=B\). In all cases \(U\) is a unit in
this \(H\)-adic completed Laurent Ore algebra.

For completeness, the recursion is elementary. If the
factorization holds through order \(n-1\), let \(E_n(T)\)
be its remaining coefficient at order \(H^n\).
Divide the Laurent polynomial \(E_n/(aT^r)\), modulo \(C_0\),
into a remainder of degree less than \(e\) and a Laurent
multiple of \(C_0\). This division is possible and unique
because \(C_0\) is monic with nonzero constant term.
Choose the remainder as \(C_n\) and the multiple, multiplied
by \(aT^r\), as \(U_n\). At this order the product is
commutative; all lower-order Ore corrections are already in
\(E_n\). This proves (11) inductively.

The \(T\)-support of \(U\) and \(U^{-1}\) need not remain
bounded as the \(H\)-order grows, and no convergence at \(H_N\)
is asserted. Coefficients can have increasing pole orders
at the classical meridian divisors.

In particular finite truncation does not replace the actual
equation by \(\widehat C R_N=\text{known source}\).
For any fixed truncation order \(m\), multiplying the exact
equation by the truncated formal inverse gives the genuine
identity, on a fixed regular coefficient chart,
\[
 \widehat C^{<m}R_N
    =(U^{-1})^{<m}\beta_N-H_N^m E_{m,N}R_N .
 \tag{12}
\]
Here \(E_{m,N}\) is the exact remainder operator defined by
the finite truncated product, with finite shift support for
this fixed \(m\). Its last term contains the unknown whole
period. A fixed \(m\) supplies only a power of \(N^{-1}\),
not a fixed exponential gap. Controlling orders growing
with \(N\), all shifted domains, and the original source
would require additional analytic estimates. Equations
(6)–(7) show why an exact finite homogeneous repair within
the same ideal cannot instead remove that remainder when
\(r>0\).

## 5. A uniform coefficient-space dimension bound

Write the same fixed operator by powers of the meridian:
\[
 B=\sum_{s=s_-}^{s_+}Y^s p_s(q,T),\qquad
 p_{s_-}\ne0.
 \tag{13}
\]
Multiplying the equation by \(Y^{-s_-}\), put
\(w=s_+-s_-\) and
\(\widetilde p_j=p_{s_-+j}\).
If \(R(Y)=\sum_k c_kY^k\), the exact coefficient recurrence is
\[
 \sum_{j=0}^{w}
   \widetilde p_j(q_N,Q_N^{k-j})c_{k-j}
        =[Y^k](Y^{-s_-}\beta_N).
 \tag{14}
\]
The \(k-j\) in the shift eigenvalue is essential: \(T\)
acts before the displayed multiplication by \(Y^j\).

Let
\[
 D=\operatorname{span}_T p_{s_-}.
 \tag{15}
\]
For all sufficiently large levels,
\(p_{s_-}(q_N,L)\) is a nonzero Laurent polynomial. Indeed
at least one of its nonzero fixed Laurent \(q\)-coefficients
has only finitely many zeros among the distinct \(q_N\).
After a Laurent monomial is removed, this polynomial has
degree \(D\), so at most \(D\) distinct nonzero roots.

**Proposition 3.** The space of Laurent polynomials supported
in \([-AN,AN]\) and annihilated by \(B(q_N,Y,T_N)\) has
dimension at most
\[
                              (2A+1)D .                   \tag{16}
\]
The solution set of (14) for any specified affine source
is either empty or a translate of a space with that bound.
The original source is nonempty because its actual \(R_N\)
is a solution.

To prove this, start with \(c_k=0\) below \(-AN\) and
advance (14) in increasing \(k\). Whenever the pivot
\(p_{s_-}(q_N,Q_N^k)\) is nonzero, \(c_k\) is uniquely
determined by preceding coefficients and the source.
At a zero pivot allow \(c_k\) as a free parameter; the
remaining equation may impose further constraints, which
can only reduce the dimension.
There are at most \(D\) such residue classes modulo \(N\).
The interval \([-AN,AN]\) meets each class at most \(2A+1\)
times. Equations above the upper support endpoint impose
additional constraints and cannot add parameters. This
proves (16).

This is a finite-dimensional reduction for the actual
equation and includes all coefficient endpoints. It uses
neither classical end preservation nor a root separation
estimate. It also shows that \(D=0\) makes the homogeneous
polynomial solution space zero; for the homogeneous actual
normal state, which is nonzero, such a pivot is impossible
at all sufficiently large levels.

Dimension alone supplies no conditioning estimate. The
nonzero pivots in (14) may be small, and forward products
are not bounded by the count of zero pivots. In particular
(16) does not imply a uniformly bounded zero multiplicity
at \(Y=1\), a finite-jet norming inequality, or a
subexponential microscopic observation constant.

## 6. Remaining concrete distinction

For every actual fixed knot the original construction
provides the nonzero normal operator, affine equation (4),
paired end loss (10), and bounded-dimensional coefficient
problem (14)–(16). If its minimal normal operator has
\(r>0\), finite homogeneous left-multiple repairs cannot
make the microscopic theorem's end condition hold.
Formal reduction (11) instead leaves the actual remainder
in (12).

A quantitative coefficient-space observation estimate, or
an analytic control of that formal remainder, could remove
the end condition. Neither follows from minimality,
primitivity, or the proved Weyl symmetry. No change to the
actual Kashaev source, omission of a central factor, or
geometric-symbol identification is made here.
