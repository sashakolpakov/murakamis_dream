# Fourier polarization, the retained source, and the two fixed directions

Private analytical audit, 31 October 2026.

This checks Sections 4–5 of
/private/tmp/md-main-meridian-regular-normal-polarization-inventory.md.
The Fourier ordering, source sign, central-support distinction,
dual-number obstruction, and geometric multiplicity conclusion are
correct. To cover an arbitrary specified squared-meridian operator,
the generic coefficient field should be \(\mathbb C(q)\), with
\(Q=q^2\). Using \(\mathbb C(Q)\) instead is valid only when one
explicitly chooses the separately constructed \(Q\)-only operator.
The following formulation makes that distinction precise.

## 1. Generic coefficients without parameter descent

Work in

$$
\mathcal R_q=
\mathbb C(q)\langle Y^{\pm1},T^{\pm1}\rangle,
\qquad TY=q^2YT,\qquad Q=q^2.
\tag{1}
$$

The shift fixes the coefficient parameter \(q\). Given an actual
squared-meridian annihilator with rational coefficients, clear
denominators and remove a fixed shift to write

$$
P=\sum_{j=0}^d a_j(q,Y)T^j,\qquad
a_j(q,Y)=\sum_m a_{jm}(q)Y^m,\qquad a_0a_d\ne0.
\tag{2}
$$

One may additionally clear the finitely many \(q\)-denominators so that
all \(a_j\) are Laurent polynomials in \(q,Y\). The actual fixed-color
functions are \(C_n(Q)\), as proved in the original finite-color
construction, so here they are evaluated as \(C_n(q^2)\). The chosen
operator itself need not be invariant under \(q\mapsto-q\).

For each fixed \(n\ge1\), the actual root equations and ordinary-color
pointing hold at infinitely many \(q_N=e^{\pi i/N}\). They therefore
give the generic rational identity

$$
\sum_{j=0}^d a_j(q,q^{2n})C_{n+j}(q^2)=0.
\tag{3}
$$

This is the usual cross-level rigidity for one fixed color index;
it does not identify a sequence of root operators with an arbitrarily
chosen classical quantization.

Let \(A_q\) be the \(q\)-exponent span of the collected monomials
in \(a_d(q,Y)\). Substituting \(Y=q^{2r}\) sends \(q^uY^v\) to
\(q^{u+2rv}\). Distinct monomials with \(v\ne v'\) can collide only if

$$
2r|v-v'|=|u-u'|\le A_q.
\tag{4}
$$

Thus \(a_d(q,q^{2r})\ne0\) whenever \(r>A_q/2\). A safe fixed start is
\(n_0\ge d+\lfloor A_q/2\rfloor+1\). The less sharp choice
\(n_0\ge d+A_q+1\) also works.

If the supplied operator really has coefficients in
\(\mathbb C(Q)[Y^{\pm1}]\), the original argument applies with its
\(Q\)-exponent span \(A_Q\) and \(n_0\ge d+A_Q+1\). Both versions
give the same conclusions. They must not be conflated by assigning
an arbitrary \(q\)-rational operator \(Q\)-rational coefficients.

## 2. The exact ordered Fourier map and its nonzero source

Put \(Sg(X)=g(QX)\). The Fourier map fixes \(q\) and sends

$$
\Phi(Y)=S,\qquad \Phi(T)=X^{-1},\qquad
X^{-1}S=QSX^{-1}.
\tag{5}
$$

Consequently

$$
A=\Phi(P)=
\sum_{j,m}a_{jm}(q)Q^{-mj}X^{-j}S^m.
\tag{6}
$$

The sign and power in \(Q^{-mj}\) follow from
\(S^mX^{-j}=Q^{-mj}X^{-j}S^m\). The map is an algebra map, not an
anti-homomorphism.

For the actual series
\(Z(q,X)=\sum_{n\ge n_0}C_n(q^2)X^n\), summing (3) yields

$$
AZ=\mathcal B,\qquad
\mathcal B=
\sum_{j,m}a_{jm}(q)Q^{-mj}X^{-j}
\sum_{r=n_0}^{n_0+j-1}C_r(q^2)Q^{mr}X^r.
\tag{7}
$$

The source has a plus sign: it consists of the initial terms removed
when rewriting each shifted tail in terms of \(Z\). The source powers
range from \(n_0-d\) to \(n_0-1\), and only \(j=d,r=n_0\) contributes
to the lowest one. Hence

$$
[X^{n_0-d}]\mathcal B
=C_{n_0}(q^2)a_d(q,q^{2(n_0-d)})\ne0.
\tag{8}
$$

The first factor is nonzero since \(C_{n_0}(1)=1\); the second is
nonzero by (4). The lowest coefficient is a fixed nonzero rational
function of \(q\), so only finitely many roots \(q_N\) are its zeros
or poles. It follows that \(\mathcal B_N\) is nonzero as a rational
function of \(X\) for every sufficiently large \(N\). This does not
mean it is nonzero at every numerical \(X\).

A fixed left power of \(S\) may shift the \(S\)-support of \(A\) to
\(0,\ldots,r\). The same power must act on \(\mathcal B\).
It preserves source nonvanishing, and preserves \(A(1)=0\) whenever
that identity holds.

## 3. The two central divisors and the finite intersection

At \(q=q_N\), put \(U=Y^N,V=T^N\) and
\(U_X=X^N,V_X=S^N\). Equation (5) gives

$$
\Phi(U)=V_X,\qquad \Phi(V)=U_X^{-1}.
\tag{9}
$$

The rational meridian realization \(\mathbb C(Y)\), with \(T\) acting
by root shift, is supported on \(V=1\), with \(U\) variable. Its Fourier
image is therefore supported on \(U_X=1\), with \(V_X\) variable.
The rational Mellin realization \(\mathbb C(X)\), with \(S\) acting
by root shift, is instead supported on \(V_X=1\), with \(U_X\) variable.
In the original coordinates its divisor is \(U=1\), with \(V\) variable.

These are different rational realizations. An isomorphism over the
fixed root center preserves the central annihilator ideal and cannot
identify the two generic supports merely by renaming variables.
The Fourier automorphism of the unlocalized tori itself is unaffected.

At \(U=V=1\), the finite map is exactly

$$
\mathscr F_N(h)=
\sum_{r=0}^{N-1}h(Q_N^r)X^r
\quad\text{in }\mathbb C[X]/(X^N-1).
\tag{10}
$$

Here \(h\) is a function on the finite orbit, for example a Laurent
polynomial modulo \(Y^N-1\); a rational representative must be regular
on that orbit. Direct multiplication and cyclic reindexing prove
\(\mathscr F_N(Yh)=S\mathscr F_N(h)\) and
\(\mathscr F_N(Th)=X^{-1}\mathscr F_N(h)\).

The actual knot state is regular there. Its image is
\(K_N+\sum_{r=1}^{N-1}C_r(q_N)X^r\) modulo \(X^N-1\).
Root periodicity gives the selected rational lift

$$
(1-X^N)(Z_N+p_<)
=\sum_{r=1}^{N-1}C_r(q_N)X^r+K_NX^N,
\quad p_<=\sum_{1\le r<n_0}C_r(q_N)X^r,
\tag{11}
$$

for \(N\ge n_0\). The numerator tends to leading ratio \(-K_N\)
after division by \(1-X^N\). With the usual residue convention,
\(\operatorname{Res}_{X=\infty}Z_N\,dX/X=K_N\). The polynomial \(p_<\)
has no constant term and contributes no residue at infinity.

The stated linear map from the ramified normal fiber to (11) is
correct: it reads the ordinary values from
\(a_{0,r}/(Q_N^r-1)\), \(r\ne0\), and \(K_N\) from
\((N/2)e_0^*b_0\). It discards the other normal coordinates and higher
jets, so it is not a comparison of the complete normal modules.

## 4. The dual-number lift obstruction

Set \(Q=Q_N(1+\varepsilon)\), \(\varepsilon^2=0\). For a
\(q\)-rational presentation this means choosing the unique local branch

$$
q=q_N(1+\varepsilon/2).
\tag{12}
$$

No global \(Q\)-descent is required. In the quantum torus,

$$
VU=Q^{N^2}UV=(1+N^2\varepsilon)UV.
\tag{13}
$$

If a finite free matrix realization lifted the clock fiber with both
\(U,V\) reducing to the identity, write
\(U=I+\varepsilon A_1\), \(V=I+\varepsilon B_1\).
Their commutator is zero, whereas (13) makes it
\(N^2\varepsilon I\). This is impossible in characteristic zero.
For \(N\)-dimensional invertible clock matrices the determinant also
forces \(Q^N=1\), contrary to \(Q^N=1+N\varepsilon\).

The obstruction concerns a finite free clock-matrix lift. It does not
exclude a comparison using differential normal operators, a larger
module, or relative source data. Those qualifications in the draft
are necessary and correctly stated.

## 5. Two independent fixed directions in the canonical Mellin companion

For the positive-volume knots under discussion, every polynomial
reduced annihilator has \(P=B(Y-1)\). Thus

$$
A=\Phi(B)(S-1),\qquad A(1)=0.
\tag{14}
$$

After the common \(S\)-shift, \(A\) has support \(0,\ldots,r\), with
nonzero endpoint coefficients. Here \(r\ge1\): an order-zero nonzero
multiplication operator cannot kill \(1\). This supplies the first
two jet coordinates used below.

Retain the canonical sourced homogenization

$$
\widehat A=(S-\sigma\mathcal B/\mathcal B)A.
\tag{15}
$$

Both \(1\) and the actual rational \(Z_N\) solve (15). They are
independent over the fixed field \(\mathbb C(X^N)\), since a central
\(Z_N\) would satisfy \(AZ_N=Z_NA(1)=0\), contrary to
\(\mathcal B_N\ne0\).

They give independent vectors even over \(E=\mathbb C(X)\) in the
companion of order \(r+1\). Indeed a dependence between
\(J1=(1,\ldots,1)^t\) and
\(JZ_N=(Z_N,SZ_N,\ldots,S^rZ_N)^t\) would, from its first two
coordinates, give \(SZ_N=Z_N\). This again makes \(Z_N\) central.

If \(C_N\) is the forward companion and
\(\mathsf T_0=C_N^{-1}S\), both vectors are fixed by \(\mathsf T_0\).
They are therefore fixed by the \(E\)-linear root monodromy
\(H_0=\mathsf T_0^N\). Consequently

$$
\dim_E\ker(H_0-I)\ge2,\qquad
\left.\partial_t\det(tI-H_0)\right|_{t=1}=0.
\tag{16}
$$

This is geometric multiplicity in its linear-algebra sense. It
identifies no geometric knot-\(A\) factor and asserts no Jordan block.
The result concerns this canonical sourced Mellin presentation,
not the primitive minimal meridian companion.

All fixed rational coefficients and both endpoints specialize
nontrivially for every sufficiently large \(N\); their exceptions
form a finite set of parameter values. No numerical \(X\)-evaluation
is used to discard an apparent pole.

The observable row is also correctly normalized:
if \(A=\sum_{j=0}^r a_jS^j\), put
\(\ell=\mathcal B^{-1}(a_0,\ldots,a_r)\).
The coefficient identity in (15) gives
\(\sigma(\ell)C_N=\ell\). Therefore

$$
\ell(H_0-I)=0,\qquad \ell J1=0,\qquad \ell JZ_N=1.
\tag{17}
$$

The selected source is visible despite multiplicity at least two.
The constant solution is excluded by the actual starting lattice
\(X^{n_0}\mathbb C[[X]]\); its rational companion existence does not
contradict uniqueness in that lattice.

## 6. The unknot example and the recommended wording

For the genuine unknot annihilator \((T-1)^2\) and \(n_0=3\),

$$
Z=\frac{X^3}{1-X},\qquad
A=(X^{-1}-1)^2,\qquad
AZ=X(1-X).
\tag{18}
$$

This verifies the sign and order in the displayed example.
The original meridian companion has a nontrivial unipotent Jordan
block, whereas the sourced Mellin homogenization has order one and
its observable row detects the selected state. The example is
outside the positive-volume hypothesis and does not contradict
(16); it illustrates dependence on the realization and its source.
The rational gauge by \(Y-1\) carries the generic meridian Jordan
statement to the normal state, without licensing a specialization
that discards the meridian zero.

For the focused statement, the safe choices are:

* use \(\mathbb C(q)\) with \(Q=q^2\), (4), and (12) throughout,
  covering every supplied squared-meridian operator; or
* explicitly choose the separately proved \(Q\)-only operator and
  retain the narrower \(\mathbb C(Q)\) notation.

Two small expository qualifications are useful: (10) is on the finite
regular orbit fiber, and the covered-class transformed operator has
positive \(S\)-order because it kills \(1\). With these stated, the
claims in Sections 4–5 are sound and retain their asserted scope.
