# Physical-row eigenvectors and failure of Fourier positivity after multiplication

Private written proof, 17 November 2026.

An individual physical kernel row is an exact eigenvector of every
signed turn, with its original unit scalar. This favorable behavior
does not extend to products of rows. For every level \(N\ge5\), the
ordinary product of two copies of the first nonconstant physical row
has strictly positive Laurent coefficients and one repeated real root
greater than two. Either original unit turn sends it to a quadratic
whose Laurent coefficients cannot all be made real by a common phase.
It also acquires a nonreal spectral zero.

The input is an actual two-incidence kernel product, not an arbitrary
coupon. The calculation is in the full algebra and retains every
normal. It rules out preservation of this positive Fourier or
real-root class under the original operations. It does not assert
a zero of an eligible knot scalar or a failure of its asymptotic
lower bound.

## 1. Original conventions and isolated physical rows

Put
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 s_k=2\sin(k\pi/N),\quad S_k=\prod_{a=1}^k s_a,\quad
 c_j=q^{2j+1}+q^{-2j-1},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 e_k(Z)=S_k^{-2}\prod_{a<k}(c_a-Z),\qquad
 K_N(w,Z)=\sum_{k=0}^{D}e_k(w)e_k(Z).
 \tag{1}
\]
Here \(T_N\) in the relation is the ordinary Chebyshev polynomial.
The physical turn is \(Te_k=e_{D-k}\). Multiplication and inversion
of the original crossing \(R\) take place in
\(\mathcal A_N=\mathbb C[Z]/(P_N)\), retaining its double roots.
For every integer \(n\), define the original signed operator
\[
                V_n=\kappa^n T R^{-n}T .
 \tag{2}
\]
Thus \(V_0=I\), \(V_{\sigma}=U_\sigma\) for \(\sigma=\pm1\),
and \(V_{n+m}=V_nV_m\). No carrier is omitted. Ordinary products
below are products in the spectral variable, followed by canonical
reduction only if needed.

Let
\[
 J_N=\lfloor(N-1)/2\rfloor,\qquad
 F_j(Z)=K_N(c_j,Z),\quad 0\le j\le J_N.
 \tag{3}
\]
These are the distinct physical rows. Their degrees are exactly \(j\):
the terms with \(k>j\) vanish because \(e_k(c_j)=0\), while
\(e_j(c_j)>0\). The latter follows from
\(c_a-c_j=4\sin((j+a+1)\pi/N)\sin((j-a)\pi/N)>0\)
for \(0\le a<j\le J_N\).

**Proposition 1.** At every level and for every signed integer \(n\),
\[
 \boxed{\qquad
 V_nF_j=\lambda_{n,j}F_j,\qquad
 \lambda_{n,j}=(-1)^{nj}q^{-nj(j+1)} .
 \qquad}
 \tag{4}
\]
This is an equality of ordinary canonical polynomials, and hence
includes every physical first normal.

**Proof.** The exact reproducer identity gives
\[
 TF_j=\delta_{c_j},\qquad
 \delta_{c_j}(Z)=\frac{P_N(Z)}{\eta N^2(Z-c_j)}.
 \tag{5}
\]
The quotient in (5) is an ordinary polynomial. For every polynomial
\(p\),
\((p(Z)-p(c_j))\delta_{c_j}\) is divisible by \(P_N\).
Consequently \(R^{-n}\delta_{c_j}=R(c_j)^{-n}\delta_{c_j}\)
in the full quotient, and
\[
                   V_nF_j=\kappa^nR(c_j)^{-n}F_j .
 \tag{6}
\]
This argument uses divisibility by the entire relation, with its
multiplicities, rather than only equality of distinct-node values.
It works also at the odd simple row.

To evaluate the scalar without changing its crossing convention,
use the exact triangular unit-turn matrix:
\[
 [e_r]U_\sigma e_k
   =(-1)^kq^{-\sigma k(r+1)}
                      \frac{S_k}{S_rS_{k-r}}\quad(r\le k).
 \tag{7}
\]
Its degree-\(j\) diagonal is
\((-1)^jq^{-\sigma j(j+1)}\). Since \(F_j\) has degree \(j\),
comparison of leading coefficients in (6) proves (4) for a unit
turn. Taking integer powers, including the inverse, proves it for
all \(n\). The operators preserve degree by (7), so the quotient
identity is also the asserted ordinary polynomial identity.
\(\square\)

## 2. The exact two-incidence product

Assume \(N\ge5\), and abbreviate \(c=c_0=2\cos(\pi/N)\).
The first two physical-row recurrence steps are nonsingular, including
when \(F_2\) is the odd simple row at \(N=5\). Write
\[
 A_0=\frac{s_1^3}{s_2},\qquad
 A_1=\frac{s_2^4}{s_3s_4},\qquad
 C_1=\frac{s_1^4}{s_2s_3}.
 \tag{8}
\]
These are positive. With \(X=c-Z\), the original recurrence is
\[
 F_0=1,\qquad F_1=1+\frac{X}{A_0},\qquad
 A_1F_2=(A_1+C_1+X)F_1-C_1 .
 \tag{9}
\]
Direct comparison of the quadratic, linear and constant terms gives
\[
 \boxed{\quad F_1^2=aF_2+bF_1+dF_0,\quad}
 \tag{10}
\]
\[
 a=\frac{A_1}{A_0},\qquad
 b=1-\frac{A_1+C_1}{A_0},\qquad
 d=\frac{C_1}{A_0}.
 \tag{11}
\]
There is no quotient reduction in this degree-two identity.

Using
\[
 s_2=cs_1,\qquad s_3=(c^2-1)s_1,\qquad
 s_4=c(c^2-2)s_1
 \tag{12}
\]
yields the explicit coefficients
\[
 \boxed{\quad
 a=\frac{c^4}{(c^2-1)(c^2-2)}>0,\qquad
 b=-\frac4{c^2-2}<0,\qquad
 d=\frac1{c^2-1}>0 .
 \quad}
 \tag{13}
\]
Here \(c^2>2\) for \(N\ge5\), and \(a+b+d=1\).
In particular even this first product does not have nonnegative
linearization coefficients in the physical-row eigenbasis.

The input nevertheless has the desired stronger positivity in its
ordinary Fourier coordinates. Since
\[
 A_0=\frac{4-c^2}{c},\qquad
 F_1(Z)=\frac{4/c-Z}{A_0},
 \tag{14}
\]
its root \(4/c\) is strictly greater than two. For
\(\zeta=e^{it}\), \(Z=-(\zeta+\zeta^{-1})\),
\[
          F_1(Z)=\frac{4/c+\zeta+\zeta^{-1}}{A_0}.
 \tag{15}
\]
All five Laurent coefficients of \(F_1^2\), from degree \(-2\)
through degree \(2\), are strictly positive. Thus (10) does not
start with a sign-indefinite Fourier input.

## 3. Failure after either unit turn, and after every fixed nonzero power

Proposition 1 and (10) give, exactly for every integer \(n\),
\[
 \boxed{\quad
 q^{6n}V_n(F_1^2)
     =aF_2+b(-1)^nq^{4n}F_1+dq^{6n}.
 \quad}
 \tag{16}
\]
Every equality is in ordinary degree at most two, hence also in the
full physical algebra without any omitted normal.

**Theorem 2.** If \(N\ge5\) and
\(\sin(4\pi n/N)\ne0\), no nonzero scalar makes all Laurent
coefficients of \(V_n(F_1^2)(-\zeta-\zeta^{-1})\) real.
In particular no unit phase makes them nonnegative.
This applies to \(n=1\) and \(n=-1\) at every \(N\ge5\).
For every fixed \(n\ne0\), it applies at every \(N>4|n|\)
with \(N\ge5\).

**Proof.** Let \(L_k(f)\) denote the coefficient of \(\zeta^k\)
in \(f(-\zeta-\zeta^{-1})\). Equation (9) gives
\[
 L_2(F_2)=\frac1{A_0A_1}>0,\qquad
 L_1(F_1)=\frac1{A_0}>0 .
 \tag{17}
\]
All coefficients of \(F_2\) are real. In the phase normalization
of (16), the degree-two coefficient is
\[
             aL_2(F_2)=\frac1{A_0^2}>0.
 \tag{18}
\]
Its degree-one coefficient has imaginary part exactly
\[
       \frac{b(-1)^n}{A_0}\sin(4\pi n/N)\ne0.
 \tag{19}
\]
Any scalar making (18) real must itself be real in this
normalization. It cannot make the coefficient in (19) real.
This proves the claim. For unit signs,
\(0<4\pi/N<\pi\); the fixed-power assertion follows from
\(0<4\pi|n|/N<\pi\). At finite resonances where the sine
vanishes, the theorem makes no assertion.
\(\square\)

**Corollary 3.** Under the same hypotheses, \(V_n(F_1^2)\)
has a nonreal spectral zero. Thus the class of polynomials with
all roots in \((2,\infty)\), or the corresponding zero-free class
on \(\mathbb C\setminus[2,\infty)\), is not preserved.

**Proof.** It is a quadratic with nonzero leading coefficient.
After the phase normalization (16), that leading coefficient in
\(Z\) is positive real by (18). Its coefficient of \(Z\) is
nonreal by (19): the \(Z^2\) term contributes only Laurent
degrees two, zero and minus two. If both roots were real, the
monic quadratic would have real coefficients. This contradiction
proves the corollary. \(\square\)

There is an important scale limitation. For fixed \(n\), put
\(x=(c-Z)/A_0\). From (9)--(13), the polynomial (16) is
\[
 x^2+\{2-b+b(-1)^nq^{4n}\}x
              +a+b(-1)^nq^{4n}+dq^{6n}.
 \tag{20}
\]
Its coefficients are bounded as \(N\to\infty\). Its roots in \(x\)
are therefore bounded, while \(A_0=O(N^{-2})\) and
\(c=2+O(N^{-2})\). The spectral zeros in Corollary 3 satisfy
\[
                              Z=2+O_n(N^{-2}).
 \tag{21}
\]
They do not give zeros on a fixed compact positive-parent chart
away from the endpoint. No macroscopic zero or scalar closing
conclusion is inferred from this example.

## 4. What remains possible

The exact isolated-row eigenstructure (4) is useful and survives
all signed powers. The counterexample concerns its closure under
the ordinary multiplication required when two incidences meet.
Both inputs are the actual kernel \(K_N(c_1,Z)\); the subsequent
operator is exactly (2), with all carriers fixed. No change of
the original source, artificial cap, or deleted normal is used.

The calculation disproves an invariant positive-Fourier or
real-root argument for arbitrary compositions. It does not disprove
a coherent saddle estimate for a larger source class, a nonzero
coefficient of its selected geometric cycle, or the original
volume-conjecture lower bound. In particular this local source
is not asserted to be the complete scalar of an admissible fixed
short filling. The prescribed closing and its coherent phases
still require their own proof.

## Direct sources and author audit

The two complete direct texts were read, their used implications
checked, and their pins verified:

* [Exact signed-turn identities](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  original turn and crossing conventions, full triangular matrix,
  degree preservation and the ordinary reproducer (5).
* [Physical Jacobi charge boundary](research_physical_jacobi_charge_boundary.md),
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  original physical-row normalization and the two recurrence steps
  (8)--(9), with their valid endpoint ranges.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
