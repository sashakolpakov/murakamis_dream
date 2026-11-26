# Exact coefficient transport at a complete boundary

Research note, 3 November 2026.

An internal pair of filled vertices has a useful exact description in
Newton coefficients. For equal powers, its complete-boundary value is a
bilinear square. The vector in this square satisfies a difference equation
with prescribed boundary data; at power three the equation involves only
four successive shifts. This gives a concrete problem for asymptotic
analysis, with the actual finite solution fixed from the outset.

The underlying quantum character operators were established in
[the Newton character calculation](actual_newton_twist_canonical_graph.md)
and [the full crossing-transport identity](research_current_free_aw_crossing_transport.md).
The Fourier interpolation used below is the existing
[exact internal-wire interpolation](research_internal_wire_exact_circle_averaging.md).
The purpose here is to specialize those identities to the complete-boundary
coefficient vector, calculate its forcing and normalization, and distinguish
its bilinear square from the positive norm obtained by reversing one power.
Section 6 now records the separately proved full internal \(3,3\)
packet, including its two free boundaries. Its nonzero coefficient
comes from the exact complex-circle analysis, not from the recurrence
or the positive opposite-power norm alone. The general short-power
connection problem remains open.

## 1. The original pair and its coefficient vector

Fix an integer \(N\ge2\), and put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},\quad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
The fractional power in \(\kappa\) uses the displayed logarithm of
\(q\). Write
\[
 \begin{split}
 c_j&=2\cos((2j+1)\pi/N),\\
 P_N(z)&=2T_N(z/2)+2=\prod_{j=0}^D(z-c_j),\\
 e_j(z)&=S_j^{-2}\prod_{r<j}(c_r-z),\\
 \mathcal A_N&=\mathbb C[z]/(P_N),\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \end{split}
 \tag{2}
\]
Here \(T_N\) is the ordinary Chebyshev polynomial. The full Frobenius
pairing is \(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\). Its matrix is the
reversal \(J\), where \(J_{ij}=\mathbf1_{i+j=D}\).

Let \(M\) be multiplication by the original positive crossing \(R\).
In this basis,
\[
 M_{jk}=\kappa(-1)^j q^{j(k+1)}
               \frac{S_j}{S_kS_{j-k}}\quad(0\le k\le j<N),
 \qquad M_{jk}=0\quad(k>j).
 \tag{3}
\]
All powers below are original signed crossing powers. For an arbitrary
free spectral variable \(z\), define
\[
 v(z)=(e_0(z),\ldots,e_D(z))^{\mathsf T},\qquad
 A_n=JM^n,\qquad w_n(z)=A_n v(z).
 \tag{4}
\]
Multiplication is self-adjoint for the Frobenius pairing, so
\((M^n)^{\mathsf T}J=JM^n\); in particular \(A_n^{\mathsf T}=A_n\).
The original edge kernel is
\(K_N(z,z')=v(z)^{\mathsf T}v(z')\).

Let the two selected vertices have powers \(n,p\), with three original
edges forming a path between the two free endpoints. Their source is
\[
 \begin{split}
 \mathcal P_{n,p,N}(z,z')
 &=\phi_N^{(x)}\phi_N^{(y)}
       [R(x)^nR(y)^pK_N(z,x)K_N(x,y)K_N(y,z')]\\
 &=v(z)^{\mathsf T}A_nA_pv(z')
  =w_n(z)^{\mathsf T}w_p(z').
 \end{split}
 \tag{5}
\]
To verify the normalization, the coefficient of the two incident
Newton modes \(i,j\) at one selected vertex is
\(\phi_N(R^n e_i e_j)=(JM^n)_{ij}\). Contract the shared index and
use symmetry of \(A_n,A_p\). There is no further level-dependent
scalar in (5).

A complete endpoint has angular parameter zero and spectral value
\(z=-2\). Abbreviate \(w_n=w_n(-2)\). For equal powers,
\[
                   \mathcal P_{n,n,N}(-2,-2)
                         =\sum_{j=0}^D w_{n,j}^{\,2}.
 \tag{6}
\]
This is a bilinear square, with no complex conjugation.

## 2. A forced equation that determines the actual vector

Let \(Z\) be multiplication by \(z\) in the Newton basis:
\[
 Z_{jj}=c_j,\qquad
 Z_{j,j-1}=-4\sin^2(j\pi/N)\quad(j\ge1).
 \tag{7}
\]
All other entries vanish. The original character operator and its
crossing conjugates are
\[
 L_0=Z^{\mathsf T},\qquad L_n=M^{-n}Z^{\mathsf T}M^n,
 \qquad \mathcal D_n=JL_{-n}J.
 \tag{8}
\]
The notation \(\mathcal D_n\) in this note denotes this matrix; it is
not a trace functional. We have \(JZJ=Z^{\mathsf T}\) and
\[
                 \mathcal D_n=A_nZ^{\mathsf T}A_n^{-1}.
 \tag{9}
\]

**Proposition 1.** At every free spectral value,
\[
 \boxed{\quad
 (\mathcal D_n-zI)w_n(z)
       =-\frac{\eta\kappa^n}{N^2}P_N(z)\,\mathbf e_0,
 \qquad w_{n,D}(z)=\kappa^n.\quad}
 \tag{10}
\]
Here \(\mathbf e_j\) is a coordinate vector, whereas \(e_j(z)\)
is a Newton polynomial. In particular,
\[
 (\mathcal D_n+2I)w_n
      =\frac{2(1-\eta)\kappa^n}{N^2}\,\mathbf e_0,
 \qquad w_{n,D}=\kappa^n.
 \tag{11}
\]
These equations determine \(w_n\) uniquely at every level. The forcing
in (11) is zero at odd levels and \(4\kappa^n/N^2\) at even levels.

*Proof.* The Newton recurrence gives
\[
 (Z^{\mathsf T}-zI)v(z)
       =(c_0-z)e_D(z)\mathbf e_D
       =-\frac{\eta}{N^2}P_N(z)\mathbf e_D.
 \tag{12}
\]
The last equality uses \(S_D=N\). Also
\(M^n\mathbf e_D=\kappa^n\mathbf e_D\), including negative \(n\).
Multiplication of (12) by \(A_n\) proves the first part of (10).
The last row of \(A_n=JM^n\) is the first row of \(M^n\), so
its product with \(v(z)\) is \(\kappa^n e_0(z)=\kappa^n\).

At \(z=-2\), \(P_N(-2)=2(1-\eta)\), and
\(-\eta(1-\eta)=1-\eta\), giving (11). If \(N\) is even,
\(-2\) is not a root of \(P_N\), so \(\mathcal D_n+2I\)
is invertible by (9). If \(N\) is odd, \(-2\) is a simple root
of \(P_N\). The kernel in (11) is then one-dimensional, again
by (9); its displayed nonzero last coordinate fixes the scalar.
This proves uniqueness. \(\square\)

Thus a quantum character equation by itself is not being used to
choose a convenient solution. Both its actual inhomogeneous term
and its normalization are specified. Formula (10) also retains the
ordinary free-boundary polynomial and its derivatives. The even-level
term must not be discarded by pretending that \(-2\) is always a
physical root.

## 3. The four-step equation at power three

The matrix \(L_1\) is explicitly tridiagonal:
\[
 \begin{split}
 (L_1)_{jj}&=4qQ^j-q(1+Q)Q^{2j},\\
 (L_1)_{j,j-1}&=(L_1)_{j-1,j}=-(1-Q^j)^2.
 \end{split}
 \tag{13}
\]
The character identities cited above give
\[
 L_{r+1}+qZL_r+q^2L_{r-1}=8qI,
 \qquad JL_{-1}J=L_1.
 \tag{14}
\]
The order of multiplication in (14) matters. Writing \(B=Z^{\mathsf T}\)
and applying the recurrence twice in the negative direction yields
\[
 \boxed{\quad
 \mathcal D_3
 =q^{-2}(B^2-I)L_1+q^{-3}BZ
                       -8q^{-2}B+8q^{-1}I.\quad}
 \tag{15}
\]
Indeed
\(L_{-2}=8q^{-1}I-q^{-1}ZL_{-1}-q^{-2}L_0\), and
\(L_{-3}=8q^{-1}I-q^{-1}ZL_{-2}-q^{-2}L_{-1}\).
Conjugate the resulting expression by \(J\) to obtain (15).
Since \(B\) is upper bidiagonal and \(L_1\) tridiagonal,
row \(j\) of (11) involves only
\(w_{3,j-1},w_{3,j},\ldots,w_{3,j+3}\), with out-of-range
coordinates omitted. Formula (15), rather than division by a
possibly vanishing row coefficient, defines the recurrence at every
index and every level.

For reference, its leading characteristic equation is also explicit.
Put \(X=e^{2\pi ix}\), and regard \(U\) as the forward ratio of a
formal exponential solution. Define
\[
 c=X+X^{-1},\quad b=c-2,\quad
 a=4X-2X^2,\quad d=-(1-X)^2.
 \tag{16}
\]
The leading equation for \((\mathcal D_3+2I)w=0\) is
\[
 \begin{split}
 F_X(U)={}&\bigl((c+bU)^2-1\bigr)
                   \bigl(a+d(U+U^{-1})\bigr)\\
 &+(c+bU)(c+bU^{-1})-8(c+bU)+10=0.
 \end{split}
 \tag{17}
\]
It follows by replacing the upper and lower shifts in (15) by
\(U,U^{-1}\), respectively. The quartic \(p_X(U)=UF_X(U)\)
has discriminant
\[
 \operatorname{disc}_U p_X
 =\frac{1024(X-1)^{12}}{X^5}
             (20X^5-64X^4+80X^3-50X^2+8X-1).
 \tag{18}
\]
If the quintic in parentheses is \(f(X)\), direct polynomial
elimination gives
\[
        \operatorname{Res}_X(f(X),X^5f(X^{-1}))
                              =-1107908637241\ne0.
 \tag{19}
\]
Its coefficients are real, so a zero on the unit circle would be
shared with its reciprocal polynomial. Equations (18)--(19) therefore
show that the four roots in (17) are distinct for every real
\(0<x<1\). The leading coefficient is nonzero there.

These are exact polynomial calculations, reproduced by
[the symbolic verifier](../experiments/check_complete_boundary_coefficient_symbol.py).
It also checks the endpoint scaling: after putting
\(U=y/(X-1)^2\), the limit of \(F_X(U)\) as \(X\to1\) is
\[
                 4-y(y+1)^2=-(y-1)(y^2+3y+4).
 \tag{20}
\]
The three divergent ratios thus have leading constants
\(1,(-3+i\sqrt7)/2,(-3-i\sqrt7)/2\); the fourth ratio tends
to zero. Distinct characteristic roots do not imply that a chosen
one supplies the asymptotic of the actual solution. In particular,
the proof above supplies no connection coefficient through regions
where their moduli agree.

The [finite quotient checker](../experiments/check_complete_boundary_coefficient_transport.py)
constructs the crossing matrix by polynomial multiplication and division
in the original algebra. It computes the vectors independently by the
Frobenius trace, then checks the displayed matrices, both parity terms,
conjugation, and the Fourier identities below. Its
[saved result](../repro/results/research-complete-boundary-coefficient-transport.json)
records 1,630 diagnostics at 100 digits for levels \(3\) through \(12\).
These are finite checks of the identities and normalizations, with no
asymptotic conclusion.

## 4. Exact Fourier averaging and the positive opposite-power pair

Let
\(\Lambda_N=\{-D/2,-D/2+1,\ldots,D/2\}\). The full quotient-valued
interpolation of an internal Newton mode is
\[
 \mathbf B_N(x)=\sum_{\ell\in\Lambda_N}\mathbf c_\ell e^{2\pi i\ell x},
 \qquad
 \mathbf c_\ell=\frac1N\sum_{j=0}^D e_j e^{-2\pi i\ell j/N}.
 \tag{21}
\]
It agrees with the canonical factorial interpolation at all full
physical jets, as proved in the internal-wire note. Define
\[
 W_{n,N}(x)=\phi_N[R^n\mathbf B_N(x)K_N(\cdot,-2)].
 \tag{22}
\]
Then \(W_{n,N}(j/N)=w_{n,j}\). Products of two such functions
have integer frequencies in \([-D,D]\). Consequently, for any
real \(a,h\),
\[
 \boxed{\quad
 \mathcal P_{n,p,N}(-2,-2)
       =N\int_{a+ih}^{a+1+ih}W_{n,N}(x)W_{p,N}(x)\,dx.\quad}
 \tag{23}
\]
This is exact character orthogonality; there are no omitted internal
index aliases or endpoint terms. The first normal data are retained
in (21)--(22).

All Newton polynomials and the trace have real coefficients, and the
actual crossing satisfies \(\overline M=M^{-1}\). Therefore
\[
 w_{-n}=\overline{w_n},\qquad
 W_{-n,N}(x)=\overline{W_{n,N}(\bar x)}.
 \tag{24}
\]
In particular the opposite-power source has the exact positive formula
\[
 \boxed{\quad
 \mathcal P_{n,-n,N}(-2,-2)
       =\sum_{j=0}^D|w_{n,j}|^2
       =N\int_0^1|W_{n,N}(x)|^2\,dx>0.\quad}
 \tag{25}
\]
Strict positivity follows already from \(w_{n,D}=\kappa^n\).
This formula reverses one of the two powers. It is not a positive
formula for (6).

The original representation also preserves a different form:
\[
 M^*JM=J,\qquad A_n^*JA_n=J,\qquad
                         w_n^*Jw_n=v(-2)^{\mathsf T}Jv(-2)=1.
\]
Here \(*\) denotes conjugate transpose. The first equality follows
from \(\overline M=M^{-1}\) and \(M^{\mathsf T}J=JM\), and the
second from \(A_n=JM^n\). For the last normalization, the exact
identity-kernel formula is
\[
 \sum_{j=0}^D e_j(z)e_{D-j}(z')
       =\frac{\eta}{N^2}\frac{P_N(z)-P_N(z')}{z-z'}.
\]
It follows either from the Newton recurrence by telescoping or from
the reproducing identity for the Frobenius pairing. At \(z=z'=-2\)
its right side is \(\eta P_N'(-2)/N^2=1\).
The reversal \(J\) has both positive and negative eigenvalues for
\(N\ge2\). Thus this preserved form is indefinite. Its value one
does not give an upper bound on the Euclidean norm or a positive
lower bound on \(w_n^{\mathsf T}w_n\). Such bounds would need
additional properties of these particular vectors.

For the half-band unitary transform
\(\widehat w_n(\ell)=N^{-1/2}\sum_j w_{n,j}e^{-2\pi i\ell j/N}\),
the corresponding formulas are
\[
 \mathcal P_{n,n,N}(-2,-2)
       =\sum_{\ell\in\Lambda_N}\widehat w_n(\ell)\widehat w_n(-\ell),
 \qquad
 \mathcal P_{n,-n,N}(-2,-2)=\sum_{\ell\in\Lambda_N}|\widehat w_n(\ell)|^2.
 \tag{26}
\]
Thus Plancherel retains the distinction between the two sources.

## 5. What positivity does and does not supply

There is an elementary obstruction to a constant-phase positive
integrand for the same-sign pair on the real Fourier period.
For \(n=3\), set \(\theta=\pi/N\) and
\[
 E=e_1(-2)=\frac1{4\sin^2(\theta/2)},\qquad
 a=\frac1{2\cos\theta}.
 \tag{27}
\]
The upper-left two-by-two block of \(M/\kappa\) is
\(\left(\begin{smallmatrix}1&0\\-q&-q^2\end{smallmatrix}\right)\).
Cubing it and using
\(q(1-q^2+q^4)=a(1+q^6)\) gives
\[
 w_{3,D}=\kappa^3,\qquad
 \frac{w_{3,D-1}}{\kappa^3}=-q^6(E+a)-a.
 \tag{28}
\]
For \(N\ge13\), both the real and imaginary parts of the second
ratio are strictly negative. Its square therefore has strictly
positive imaginary part. The two nonzero summands
\(w_{3,D}^2\) and \(w_{3,D-1}^2\) cannot have a common phase.
In particular, there are no unit scalar \(\lambda\) and nonnegative
weights \(d_j\) with
\(w_{3,j}=\lambda d_j\overline{w_{3,j}}\) for every \(j\).
Nor can \(W_{3,N}(x)^2\) have one nonnegative phase for all real
\(x\), since its sampled values include those two squares.

This obstruction concerns exact positivity. It does not exclude
approximate phase agreement in the indices that dominate the norm.
To state the quantitative issue, put
\[
 \mathfrak c_{n,N}
    =\frac{|\mathcal P_{n,n,N}(-2,-2)|}
                  {\mathcal P_{n,-n,N}(-2,-2)}
    =\frac{|w_n^{\mathsf T}w_n|}{\|w_n\|_2^2}\in[0,1].
 \tag{29}
\]
The upper bound is Cauchy--Schwarz. With \(u_n=w_n/\|w_n\|_2\),
\[
 \min_{|\lambda|=1}\|u_n-\lambda\overline{u_n}\|_2^2
                          =2(1-\mathfrak c_{n,N}).
 \tag{30}
\]
Thus an almost-invariance assertion under conjugation would be a
precise sufficient condition for \(\mathfrak c_{n,N}\to1\).
A weaker bound \(\mathfrak c_{n,N}\ge e^{-o(N)}\) would suffice
to transfer the exponential rate of the positive norm to the
same-sign source. Neither bound follows from (23), (26), or the
exact recurrence. Even the norm's exponential rate must be identified
with the intended geometric quantity before such a transfer can
prove a volume identity.

The Schwarz relation (24) changes the crossing sign. Shifting the
circle in (23) leaves a product of two same-sign functions when
\(n=p\); it does not insert a conjugate. A different contour or a
different inner product could be useful, but its positivity and its
relation to the original cycle would require an additional argument.
No obstruction to every possible deformed contour is claimed here.

## 6. The proved internal \(3,3\) packet and the remaining scope

The first entry is a known terminal source:
\[
                    w_{n,0}=\phi_N[R^nK_N(\cdot,-2)]
                                      =H_{n,N}(0).
 \tag{31}
\]
The existing terminal theorem gives its nonzero geometric packet for
\(|n|\ge2\). Likewise, the isolated degree-two theorem controls
the reconstructed boundary polynomial
\(\sum_jw_{n,j}e_j(-2\cos u)\) near \(u=0\). These statements
do not by themselves give a uniform asymptotic for the individual \(w_{n,j}\)
at indices proportional to \(N\), or for (22) on a suitable complex
circle. Inverting that boundary reconstruction requires values away
from the complete endpoint and can change the exponential estimate.

For \(n=3\), that complex-circle problem is now settled by the
[mixed-source theorem](research_internal_pair_three_mixed_packet.md)
and the [full two-boundary assembly](research_internal_pair_three_full_boundary_packet.md).
With an outside angle \(u\), write
\[
 W_{3,N}(x,u)=
 \phi_N[R^3\mathbf B_N(x)K_N(\cdot,-2\cos u)].
\]
At the selected point \(x_*\), with \(\Im x_*>0\), the actual source has
\[
 W_{3,N}(x,u)
   =C_{N,3}N^{-1}A(x,u)e^{NS(x,u)}(1+O(N^{-1})),
 \qquad C_{N,3}=e^{3\pi i(N-1)^2/(4N)}.
\]
Here \(A\ne0\), \(S_x(x_*,0)=0\), and \(\Re S_{xx}(x_*,0)<0\).
The proof bounds the whole rest of the exact period at height
\(\Im x_*\), including the physical outer-wire tails, trace endpoint
currents and both level parities. It does not assume a geometric
packet for each bare complex edge kernel.

Apply the free-boundary version of (23). The shared critical point
\(x(u,v)\) solves \(S_x(x,u)+S_x(x,v)=0\), and the resulting theorem is
\[
 \mathcal P_{3,3,N}(-2\cos u,-2\cos v)
   =C_{N,3}^{\,2}N^{-3/2}\mathcal A(u,v)
                e^{N\mathcal S(u,v)}(1+O(N^{-1})),
 \qquad \mathcal A(u,v)\ne0,
\]
on a fixed complex bidisk, where
\[
 \mathcal S(u,v)=S(x(u,v),u)+S(x(u,v),v),\qquad
 \mathcal A(0,0)=
   \sqrt{\frac{\pi}{-S_{xx}(x_*,0)}}\,A(x_*,0)^2.
\]
The factor \(N^{-3/2}\) is exactly
\(N\cdot N^{-2}\cdot N^{-1/2}\): the circle normalization, the
two mixed-source factors, and the shared Gaussian. In particular,
with \(M_{\rm pair}=\Re\mathcal S(0,0)\), there are constants
\(c_-,c_+>0\) such that, for all sufficiently large integer levels,
\[
 c_-N^{-3/2}e^{NM_{\rm pair}}
 \le |\mathcal P_{3,3,N}(-2,-2)|
 \le c_+N^{-3/2}e^{NM_{\rm pair}}.
\]
The marked action gives
\(2\pi M_{\rm pair}=\operatorname{Vol}Y_{3,3}\) for the original
partial exterior with both outside cusps complete.

The same theorem retains all fixed ordinary boundary derivatives and
the original physical first normals. It also proves the whole-period
bound
\[
 |\mathcal P_{3,3,N}(-2\cos(u+is),-2\cos(v+it))|
 \le CN^a e^{N\{M_{\rm pair}
       -c(1-\cos u)-c(1-\cos v)+B(s^2+t^2)\}}
\]
for real \(|u|,|v|\le\pi\) and a fixed thin complex strip.
Conjugation gives the corresponding \((-3,-3)\) packet.
These are the boundary estimates needed for this particular short
block; they are stronger than a complete-point scalar lower bound.

The earlier radical and traced-midpoint bounds remain valid upper
bounds on particular sectors. They alone did not determine the
coefficient. The new nonzero coefficient is supplied by the selected
complex Gaussian together with bounds on every other part of its
original cycle. No comparison with the opposite-power norm (25),
and no lower bound for \(\mathfrak c_{3,N}\), is assumed or inferred.
For arbitrary short \(n,p\), equations (11) and (15) still provide a
source-exact connection problem; root separation in (18) does not
settle it. This fixed two-boundary result is not stability under all
short partial fillings or the general finite-exception theorem.

## 7. Exponentially small coherence in an actual long-power family

The distinction in Section 5 can be quantitative even when both
original sources already have proved nonzero geometric asymptotics.
This section uses the
[signed long-path theorem](research_uniform_path_trace_assembly.md),
with actual original sources. It does not use the internal \(3,3\)
packet of Section 6 or assert its coherence ratio.

For an arbitrary nonzero vector \(w\), its exact conjugation defect is
\[
 \|w-e^{i\vartheta}\overline w\|_2^2
   =2\|w\|_2^2
       -2\Re\!\left(e^{-i\vartheta}w^{\mathsf T}w\right).
 \tag{32}
\]
Consequently, a bound by
\(2(1-\delta_N)\|w\|_2^2\), with \(0<\delta_N\le1\), implies
\(|w^{\mathsf T}w|\ge\delta_N\|w\|_2^2\). A subexponential
lower bound \(\delta_N\ge e^{-o(N)}\) preserves the exponential
rate of the norm square. This is a criterion in the actual
coefficient norm, with the actual phases. Optimizing the scalar
phase gives exactly (30), so it does not by itself supply an
independent estimate of the required coefficient.

**Theorem 2.** There is an integer \(n_0\ge64\) such that, for
every fixed integer \(n\ge n_0\), the original internal-pair
vectors in (4) satisfy
\[
 \begin{split}
 \mathfrak c_{n,N}
   &=C_n e^{-N\Delta_n}(1+O(N^{-1})),\qquad C_n>0,\\
 \Delta_n
   &=\frac{16\pi^3}{n^6}+O(n^{-7})>0,\\
 \min_{|\lambda|=1}
   \frac{\|w_n-\lambda\overline{w_n}\|_2^2}{\|w_n\|_2^2}
   &=2-2C_n e^{-N\Delta_n}(1+O(N^{-1})).
 \end{split}
 \tag{33}
\]
The first and third asymptotics hold as \(N\) tends to infinity
through all integers, with \(n\) fixed. The expansion of
\(\Delta_n\) is a separate large-\(n\) statement.

*Proof.* Use the original edge phase, with its branch fixed at
the complete point:
\[
 \psi(0,0)=M_\infty,\qquad
 \psi_t(t,u)=-\frac1\pi
       \operatorname{arsinh}\!\left(\tan(t/2)\cos(u/2)\right).
 \tag{34}
\]
It is holomorphic near the origin, has real Taylor coefficients,
is even separately in \(t,u\), and is symmetric in its arguments.
Direct expansion of (34) gives
\[
 \psi(t,u)=M_\infty-\frac{t^2+u^2}{4\pi}
       -\frac{t^4+u^4}{192\pi}
       +\frac{t^2u^2}{32\pi}
       +O((|t|+|u|)^6).
 \tag{35}
\]
The complete-boundary internal-pair action is exactly
\[
 \Phi_{n,p}(t,u)=
     \psi(t,0)+\psi(t,u)+\psi(u,0)
     +\frac{i}{4\pi}(nt^2+pu^2)-i(t+u).
 \tag{36}
\]
There are three original edges and two selected vertices here.
In particular the selected degrees are both two.

To compare its critical values, set
\[
 \begin{split}
 f_n(t)&=2\psi(t,0)+\frac{int^2}{4\pi}-it,\\
 C(t,u)&=\psi(t,u)-\psi(t,0)-\psi(0,u)+M_\infty.
 \end{split}
 \tag{37}
\]
Thus \(\Phi_{n,p}=f_n+f_p-M_\infty+C\), and
\[
 C(t,u)=\frac{t^2u^2}{32\pi}
          +C_6(t,u)+O((|t|+|u|)^8),
 \tag{38}
\]
where \(C_6\) is a homogeneous degree-six polynomial with real
coefficients and only even powers of each variable.

Let \(t_n\) be the small critical point of \(f_n\).
The implicit-function theorem, applied after writing
\(t=n^{-1}T\), gives a convergent expansion for sufficiently
large real \(n\). Since
\(2\psi_t(t,0)=-t/\pi+O(t^3)\), it gives
\[
 \begin{split}
 t_n&=\frac{2\pi}{n+2i}+O(n^{-4})=a_n-ih_n,\\
 a_n&=\frac{2\pi}{n}+O(n^{-3}),\qquad
 h_n=\frac{4\pi}{n^2}+O(n^{-4}),\\
 t_{-n}&=-\overline{t_n},\qquad
 f_{-n}(t_{-n})=\overline{f_n(t_n)}.
 \end{split}
 \tag{39}
\]
The last identities follow from the real, even Taylor series.
Hence the real uncoupled critical values for \((n,n)\) and
\((n,-n)\) agree exactly.

Adding \(C\) moves each of these two critical points by
\(O(n^{-4})\): its gradient is \(O(n^{-3})\), while the inverse
uncoupled Hessian is \(O(n^{-1})\). Equivalently, the rescaled
two-variable stationary equations have an invertible limiting
diagonal Jacobian. Taylor expansion about the uncoupled critical
point then changes the stationary value, beyond evaluating \(C\)
there, by \(O(n^{-7})\). These analytic small solutions are the
geometric solutions in the signed long-path theorem, by its
uniqueness in the prescribed box.

For the degree-six term in (38), both sign choices have the same
real leading value: \(t_n=2\pi/n+O(n^{-2})\),
\(t_{-n}=-2\pi/n+O(n^{-2})\), and all variable powers are even.
Its contribution to the difference is therefore \(O(n^{-7})\).
The quartic term gives the difference explicitly:
\[
 \begin{split}
 &\Re\Phi_{n,-n}(t^*_{n,-n})
       -\Re\Phi_{n,n}(t^*_{n,n})\\
 &\quad=\frac{|t_n|^4-\Re(t_n^4)}{32\pi}
                +O(n^{-7})
       =\frac{a_n^2h_n^2}{4\pi}+O(n^{-7})
       =\frac{16\pi^3}{n^6}+O(n^{-7}).
 \end{split}
 \tag{40}
\]
Here \(t^*_{n,p}\) denotes the two-coordinate critical point,
not the uncoupled scalar \(t_n\). This proves strict positivity
of the difference \(\Delta_n\) for all sufficiently large \(n\).

For each such fixed integer \(n\), the cited long-path theorem
applies to both \((n,n)\) and \((n,-n)\), at every level parity.
Its exact source is (5). Both expansions have the power
\(N^{3(2-3)/2}=N^{-3/2}\), a nonzero leading amplitude, and a
level scalar of modulus one. Taking their absolute-value ratio,
and using the exact positivity (25) for the denominator, gives
the first line of (33), with \(C_n\) the positive ratio of the
amplitude moduli. Equation (30) gives the last line. \(\square\)

Thus even a lower bound
\(\mathfrak c_{n,N}\ge e^{-o(N)}\) fails for these actual
same-sign sources. This does not say that their geometric
coefficient vanishes: the same theorem proves it is nonzero.
The positive norm belongs to the opposite-power geometry, whose
action is strictly larger. Multiplying \(w_n\) by any nonzero
level-dependent scalar leaves \(\mathfrak c_{n,N}\) unchanged.

There is also a precise cost for changing coordinates while
preserving this original bilinear closing form.

**Corollary 3.** Fix \(n\) as in Theorem 2. Suppose
\(S_N^{\mathsf T}S_N=I\), and the transformed vector
\(\widetilde w_n=S_Nw_n\) satisfies
\[
 \frac{|\widetilde w_n^{\mathsf T}\widetilde w_n|}
              {\|\widetilde w_n\|_2^2}\ge e^{-o(N)}.
 \tag{41}
\]
Then its Euclidean condition number obeys
\[
                   \kappa_2(S_N)\ge
                       e^{N\Delta_n-o(N)}.
 \tag{42}
\]
For the exact half-band Fourier interpolation in (21)--(23),
a horizontal shift \(x\mapsto x+ih_N\) is such a map, with
\[
 \kappa_2(S_N(h_N))
       =e^{2\pi(N-1)|h_N|}.
 \tag{43}
\]
If that shifted sample vector satisfies (41), necessarily
\(\liminf_{N\to\infty}|h_N|\ge\Delta_n/(2\pi)\).

*Proof.* Pairing preservation and (33), (41) imply
\[
 \sigma_{\min}(S_N)^2
   \le\frac{\|S_Nw_n\|_2^2}{\|w_n\|_2^2}
   \le e^{-N\Delta_n+o(N)}.
 \tag{44}
\]
For a complex orthogonal matrix \(S_N^{-1}=S_N^{\mathsf T}\);
transposition preserves singular values. Its extreme singular
values are therefore reciprocal, proving (42).
The horizontal Fourier shift has the unitary diagonalization
\(S_N(h)=U_N^*\operatorname{diag}_{\ell\in\Lambda_N}
(e^{-2\pi\ell h})U_N\). Frequency reversal in the bilinear
identity (26) shows \(S_N(h)^{\mathsf T}S_N(h)=I\), and the
largest and smallest multipliers are \(e^{\pi D|h|}\) and
\(e^{-\pi D|h|}\), respectively. This proves (43) and the
stated necessary height. \(\square\)

This corollary is restricted to pairing-preserving coordinate
changes, and its last assertion to horizontal Fourier shifts.
It neither rules out a useful shift of positive height nor a
different contour with a correctly transported positive form.
It shows why a bounded-condition change of norm, or a scalar
geometric normalization alone, cannot turn this actual
same-sign source into its opposite-power norm at the same rate.

## 8. An exact difference equation for the entire Fourier interpolation

The sparse recurrence in Section 3 can be continued away from the
sampling grid without introducing aliases. The point is that its three
basic operators preserve the exact Fourier band. This property uses the
root-of-unity coefficients, at both ends of that band; it would not hold
for arbitrary multiplication of a band-limited function by a trigonometric
polynomial.

Write
\[
 \begin{split}
 \mathcal H_N&=\operatorname{span}
       \{e^{2\pi i\ell x}:\ell\in\Lambda_N\},&
 X&=e^{2\pi ix},&
 (\tau_\pm f)(x)&=f(x\pm1/N),\\
 c(X)&=qX+q^{-1}X^{-1},&
 b(X)&=X+X^{-1}-2,\\
 d(X)&=-(1-X)^2,&
 a(X)&=4qX-q(1+Q)X^2 .
 \end{split}
 \tag{45}
\]
The functions in \(\mathcal H_N\) are entire and satisfy
\(f(x+1)=\eta f(x)\). Define the analytic difference operators
\[
 \begin{split}
 \mathsf Z&=c(X)+b(X)\tau_-,\\
 \mathsf B&=c(X)+b(QX)\tau_+,\\
 \mathsf L&=a(X)+d(X)\tau_-+d(QX)\tau_+ .
 \end{split}
 \tag{46}
\]
Multiplication by the displayed coefficients is performed after the
shift. No projection back onto \(\mathcal H_N\) occurs in these formulas.

**Lemma 4.** All three operators in (46) preserve \(\mathcal H_N\).
If \(\mathcal E_Nf=(f(0),f(1/N),\ldots,f(D/N))^{\mathsf T}\), then
\[
 \mathcal E_N\mathsf Z=Z\mathcal E_N,\qquad
 \mathcal E_N\mathsf B=B\mathcal E_N,\qquad
 \mathcal E_N\mathsf L=L_1\mathcal E_N.
 \tag{47}
\]
Thus these are analytic realizations of the actual Newton matrices,
including their boundary rows.

*Proof.* Consider one mode \(f_\ell(x)=e^{2\pi i\ell x}\), and put
\(r=e^{2\pi i\ell/N}\). Its images under the first two operators are
\[
 \begin{split}
 \mathsf Zf_\ell
   &=f_\ell\{(q+r^{-1})X
           +(q^{-1}+r^{-1})X^{-1}-2r^{-1}\},\\
 \mathsf Bf_\ell
   &=f_\ell\{(q+Qr)X
           +(q^{-1}+Q^{-1}r)X^{-1}-2r\}.
 \end{split}
 \tag{48}
\]
At the top mode \(\ell=D/2\), \(r=-q^{-1}\), so the coefficient
of the escaping mode vanishes in both lines. At the bottom mode
\(\ell=-D/2\), \(r=-q\), and the other escaping coefficient
vanishes. Every remaining frequency lies in \(\Lambda_N\).

For the third operator, direct factorization gives
\[
 \mathsf Lf_\ell
 =f_\ell\left\{
    -(r+r^{-1})
    +2(q+r^{-1})(1+qr)X
    -r^{-1}(1+qr)(1+q^3r)X^2
          \right\}.
 \tag{49}
\]
Only the top two input modes could produce an escaping frequency.
At the top mode \(1+qr=0\); at the next mode \(r=-q^{-3}\),
so \(1+q^3r=0\). The linear term at that next mode remains
inside the band. This also covers \(N=2\).

At a sampling point \(x=j/N\), \(c(X)=c_j\) and
\(b(X)=-4\sin^2(j\pi/N)\). Therefore (46) gives the rows
of \(Z,B,L_1\). At \(j=0\) the coefficient of an outgoing
negative shift is \(b(1)=d(1)=0\); at \(j=D\) the outgoing
positive coefficient is \(b(Q^N)=d(Q^N)=0\).
Consequently no wraparound value, with either sign of \(\eta\),
is added to these rows. This proves (47). \(\square\)

Define the fourth-order analytic operator
\[
 \mathsf D_3
   =q^{-2}(\mathsf B^2-I)\mathsf L
      +q^{-3}\mathsf B\mathsf Z
      -8q^{-2}\mathsf B+8q^{-1}I.
 \tag{50}
\]
Its operator order is the one in (15). Let
\[
 s_N(x)=\frac1N\sum_{\ell\in\Lambda_N}e^{2\pi i\ell x}
              =\frac{\sin(\pi Nx)}{N\sin(\pi x)},
 \tag{51}
\]
with removable values filled in. Its sample vector is \(\mathbf e_0\).

**Theorem 5.** The original Fourier interpolation \(W_{3,N}\) from
(22) is the unique member of \(\mathcal H_N\) satisfying
\[
 \boxed{\quad
  (\mathsf D_3+2I)W_{3,N}(x)
     =\frac{2(1-\eta)\kappa^3}{N^2}\,s_N(x),\qquad
             W_{3,N}(D/N)=\kappa^3.\quad}
 \tag{52}
\]
The equation holds identically for every complex \(x\). At odd levels
its right side is zero. At even levels it is the displayed nonzero
entire cardinal function. There is no additional boundary or alias
term.

*Proof.* The sampling map \(\mathcal E_N:\mathcal H_N\to\mathbb C^N\)
is an isomorphism. Lemma 4 and (15) intertwine \(\mathsf D_3\)
with \(\mathcal D_3\), without changing the function space at any
intermediate operation. Thus both sides of (52) belong to
\(\mathcal H_N\), and their sampled values agree by (11).
They agree identically. Conversely, sampling any solution of (52)
gives the uniquely normalized vector of Proposition 1.
The definition (22) is its unique interpolation in \(\mathcal H_N\).
\(\square\)

This statement fixes the analytic representative: it is the existing
full interpolation of the original Frobenius trace. Agreement with an
arbitrarily chosen analytic function on the sampling grid would not
give (52).

One may also express the equation as an ordinary polynomial identity.
Put
\[
             \mathscr W_N(X)=e^{\pi iDx}W_{3,N}(x),
             \qquad X=e^{2\pi ix}.
 \tag{53}
\]
This is a polynomial of degree at most \(D\). Under this gauge,
\(\tau_+\) acts as \(f(X)\mapsto-qf(QX)\), and \(\tau_-\)
acts as \(f(X)\mapsto-q^{-1}f(Q^{-1}X)\). The three
conjugated operators are therefore
\[
 \begin{split}
 \widetilde{\mathsf Z}f(X)
       &=c(X)f(X)-q^{-1}b(X)f(Q^{-1}X),\\
 \widetilde{\mathsf B}f(X)
       &=c(X)f(X)-q\,b(QX)f(QX),\\
 \widetilde{\mathsf L}f(X)
       &=a(X)f(X)-q^{-1}d(X)f(Q^{-1}X)
                            -q\,d(QX)f(QX).
 \end{split}
 \tag{54}
\]
Their apparent negative powers cancel at \(X=0\), and they
preserve the polynomials of degree at most \(D\), by Lemma 4.
Form \(\widetilde{\mathsf D}_3\) from them in the order (50).
Then (52) is precisely
\[
 \boxed{\quad
  (\widetilde{\mathsf D}_3+2I)\mathscr W_N(X)
     =\frac{2(1-\eta)\kappa^3}{N^3}
                         \sum_{k=0}^D X^k,\qquad
       \mathscr W_N(Q^{-1})=\kappa^5.\quad}
 \tag{55}
\]
The normalization follows by evaluating the gauge at \(x=D/N\),
where \(e^{\pi iD^2/N}=\kappa^2\). Thus (55) is a normalized
polynomial difference equation for the actual source, including
the even-level forcing.

The forcing has an explicit elementary bound:
\[
 \left|
 \partial_x^k\left\{\frac{2(1-\eta)\kappa^3}{N^2}s_N(x)\right\}
 \right|
 \le \frac4{N^2}(\pi D)^k e^{\pi D|\Im x|}
                 \qquad(k\ge0).
 \tag{56}
\]
This follows term by term from (51). In particular it is polynomially
bounded on the real period. On a fixed horizontal line its possible
exponential rate is at most \(\pi|\Im x|\). Such a rate can be
compared with a proposed geometric packet without an unknown boundary
constant.

The theorem removes one ambiguity from a difference-equation approach:
the function, its finite-dimensional boundary data, and its entire
inhomogeneous term are specified. It does not prove which asymptotic
solution contributes on a complex contour. In particular, (52) does
not turn the equal-power square into the opposite-power norm, and
distinct roots in (18) still do not determine a connection coefficient.

The [Fourier-equation checker](../experiments/check_complete_boundary_fourier_equation.py)
applies the Laurent-polynomial operators without truncation or alias
projection. It checks band preservation and sampling on every monomial,
then constructs the original source from the Newton matrices and checks
(52) and (55), at both parities. The
[saved result](../repro/results/research-complete-boundary-fourier-equation.json)
contains 689 finite diagnostics at 100 digits, for levels \(2\) through
\(14\). These checks concern the exact identities; they do not estimate an
asymptotic connection coefficient.

## 9. The pinned Green equation and its exact adjoint test

The zero forcing at odd levels in (11) must not be omitted from an
all-level lower-bound argument. The original last-coordinate condition
can instead be incorporated as a rank-one pin. This gives a nonzero
forcing at both parities, with an exactly known scalar Green response.

**Proposition 6.** For \(z\in\mathbb C\), define
\[
 Q_n(z)=\mathcal D_n-zI+\mathbf e_0\mathbf e_D^{\mathsf T},
 \qquad
 Q_{\rm base}(z)=Z^{\mathsf T}-zI+
                         \mathbf e_D\mathbf e_0^{\mathsf T}.
 \tag{57}
\]
For every integer \(n\) and \(N\ge2\),
\[
 \begin{split}
 Q_n(z)&=A_nQ_{\rm base}(z)A_n^{-1},\\
 \det Q_n(z)&=N^2-\eta P_N(z),\\
 \mathbf e_D^{\mathsf T}(\mathcal D_n-zI)^{-1}\mathbf e_0
                      &=-\frac{\eta N^2}{P_N(z)} .
 \end{split}
 \tag{58}
\]
The last identity is meromorphic. In particular, at \(z=-2\),
\[
 \begin{split}
 \sigma_N&=1+\frac{2(1-\eta)}{N^2},\\
 Q_n(-2)w_n&=\kappa^n\sigma_N\mathbf e_0,\qquad
 \mathbf e_D^{\mathsf T}Q_n(-2)^{-1}\mathbf e_0=\sigma_N^{-1},\\
 \det Q_n(-2)&=N^2+2(1-\eta)>0 .
 \end{split}
 \tag{59}
\]
Thus the entire pinned spectrum, its determinant, and this scalar
Green entry are independent of the crossing power.

*Proof.* We have \(A_n\mathbf e_D=\kappa^n\mathbf e_0\) and
\(\mathbf e_0^{\mathsf T}A_n^{-1}
=\kappa^{-n}\mathbf e_D^{\mathsf T}\). These prove the similarity.
When \(P_N(z)\ne0\), solve (10) for \(w_n(z)\) and use its last
coordinate \(\kappa^n\); this proves the last line of (58).
Also
\(\det(\mathcal D_n-zI)=(-1)^NP_N(z)=-\eta P_N(z)\).
The rank-one determinant lemma now gives \(N^2-\eta P_N(z)\);
polynomial continuation covers its zeros. Equation (10) and the
same last-coordinate normalization give (59), including its
nonzero forcing at odd levels. \(\square\)

The literal horizontal Fourier shift does not repair the natural
indefinite adjoint test. Let \(U_N\) be the unitary half-band Fourier
transform in Section 4, and set
\[
 S_h=U_N^*\operatorname{diag}_{\ell\in\Lambda_N}
                 (e^{-2\pi\ell h})U_N,\quad
 f_{n,h}=S_hw_n,\quad b_h=S_h\mathbf e_0,\quad
 Q_{n,h}=S_hQ_n(-2)S_h^{-1}.
 \tag{60}
\]
Here \(f_{n,h}\) is the sample vector of \(W_{n,N}(x+ih)\);
exact Parseval gives
\(\|f_{n,h}\|_2^2=N\int_0^1|W_{n,N}(x+ih)|^2dx\).
Frequency reversal under \(J\) gives
\[
 S_h^*=S_h,\quad JS_hJ=S_{-h}=S_h^{-1},\quad
 Q_{n,h}^*=JQ_{n,h}J,\quad
 Q_{n,h}f_{n,h}=\kappa^n\sigma_N b_h .
 \tag{61}
\]
The adjoint relation uses the real boundary value \(-2\).

**Proposition 7.** The explicit trial \(v_{n,h}=Jf_{n,h}\) has
the exact forcing overlap and residual
\[
 |\langle v_{n,h},b_h\rangle|=1,\qquad
 Q_{n,h}^*v_{n,h}=\kappa^n\sigma_NJb_h .
 \tag{62}
\]
Consequently its adjoint lower bound is only
\[
 \|f_{n,h}\|_2\ge \frac1{\|b_h\|_2},\qquad
 \|b_h\|_2^2
  =\frac1N\sum_{\ell\in\Lambda_N}e^{-4\pi\ell h}
  =\frac{\sinh(2\pi Nh)}{N\sinh(2\pi h)} .
 \tag{63}
\]
The last expression has value one at \(h=0\).

*Proof.* Since \(S_h^*JS_h=J\), the overlap is
\(\langle Jf_{n,h},b_h\rangle
=w_n^*J\mathbf e_0=\overline{\kappa^n}\).
Apply (61) to obtain the residual in (62). Cauchy--Schwarz
applied to the forced equation divides its forcing overlap
\(\sigma_N\) by the residual norm \(\sigma_N\|b_h\|\), proving
(63). The sum follows because each Fourier coefficient of
\(\mathbf e_0\) has modulus \(N^{-1/2}\). \(\square\)

Normalizing this trial does not improve the estimate: its forcing
overlap becomes \(1/\|f_{n,h}\|\) and its residual becomes
\(\sigma_N\|b_h\|/\|f_{n,h}\|\). The same unknown norm cancels.
At fixed \(h\ne0\), (63) has rate \(-\pi|h|\), rather than
a positive geometric rate. The preserved indefinite norm
\(f_{n,h}^*Jf_{n,h}=1\) already supplies the stronger bound
\(\|f_{n,h}\|\ge1\).

This limitation occurs on the now-proved contour itself.
For \(n=3\), \(h=\Im x_*\), Section 6 and its full complement
bounds give
\[
 \|f_{3,h}\|_2=
 N^{-3/4}e^{N\Re S(x_*,0)}
 \left\{|A(x_*,0)|
       \left(\frac{\pi}{-\Re S_{xx}(x_*,0)}\right)^{1/4}
       +o(1)\right\}.
 \tag{64}
\]
The normalized trial in (62) therefore has an exponentially
small adjoint residual, since
\(\Re S(x_*,0)>\pi\Im x_*\), but its forcing overlap is
exponentially smaller still. The exact quotient remains (63).
This is a consequence of the established packet used to diagnose
the test, not an independent derivation of that packet's norm.

Even the complete pinned spectrum and scalar Green entry cannot
distinguish known original norm-growth rates. The signed long-path
theorem used in Section 7 and exact positivity (25) give, for
sufficiently large fixed integer \(n\),
\[
 \lim_{N\to\infty}N^{-1}\log\|w_n\|_2^2
       =M_{\rm ref}(n)
       =3M_\infty-\frac{4\pi}{n^2}+O(n^{-4}) .
 \tag{65}
\]
To verify the expansion, the three-edge action is
\[
 3M_\infty-\frac{t^2+u^2}{2\pi}
       +\frac{in(t^2-u^2)}{4\pi}-i(t+u)
       +O((|t|+|u|)^4).
\]
Its quadratic critical point is
\(t=2\pi/(n+2i)\), \(u=2\pi/(-n+2i)=-\bar t\).
The exact point differs by \(O(n^{-4})\), since the inverse
quadratic Hessian is \(O(n^{-1})\); the quadratic critical real
value is \(3M_\infty-4\pi/(n^2+4)\). This proves (65).
Hence \(M_{\rm ref}(2n)-M_{\rm ref}(n)
=3\pi/n^2+O(n^{-4})>0\) for sufficiently large \(n\), although
all the spectral and pinned Green data in (58)--(59) agree.
The missing growth is carried by the actual nonnormal eigenvectors
and Green columns, not those scalar spectral data. An eigenvalue
gap or determinant estimate therefore does not control the required
singular-value geometry or provide the independent norm lower bound.

The pin construction also applies to a literal longer original word
\(V_N\) in \(M^{\pm1},J\): conjugate \(Q_{\rm base}(-2)\) by
\(V_N\), with source \(f=V_Nv(-2)\), forcing
\(b=V_N\mathbf e_D\), and pin row
\(\ell^{\mathsf T}=\mathbf e_0^{\mathsf T}V_N^{-1}\).
Then \(Qf=\sigma_Nb\), \(\ell^{\mathsf T}f=1\), and the same
indefinite adjoint trial has \(\langle Jf,b\rangle=1\) and
residual \(\sigma_NJb\). All are identities in the full original
algebra. They do not assert that the longer word has a nonzero
geometric packet. A useful new dual construction must improve
this residual-to-forcing ratio and, for the
[Gaussian observation criterion](research_shifted_gaussian_observation.md),
also locate the resulting norm on the selected part
of the original shifted cycle.

The finite checker cited in Section 3 now also tests the pinned
conjugacy, determinant, forcing and inverse-matrix entry, as well as
the shifted adjoint identity and its forcing norm. It constructs the
reference crossing by multiplication in the original quotient algebra.
The saved 1,630 diagnostics include both level parities. These finite
checks support the exact identities; the asymptotic norm comparison
uses the written long-path proof and the expansion above.

### A boundary condition for an independent adjoint trial

There is a more elementary obstruction for trials obtained only from
a bulk Gaussian calculation. It uses the exact endpoint row, and
does not assume that the trial is a function of the unknown source.

**Proposition 8.** Let \(N\ge5\), put \(Q=Q_3(-2)\), and let
\(u\in\mathbb C^N\) with \(u_0\ne0\). If
\[
 1224\left(\sum_{j=D-3}^{D}|u_j|^2\right)^{1/2}
                         \le\varepsilon |u_0|,
 \qquad 0\le\varepsilon<1,
 \tag{66}
\]
then the lower bound obtained from this trial in the original
forced equation satisfies
\[
 \frac{\sigma_N|\langle u,\mathbf e_0\rangle|}
                          {\|Q^*u\|_2}
                    \le\frac{\sigma_N}{1-\varepsilon}.
 \tag{67}
\]
In particular a trial supported away from the last four coordinates
cannot give a positive exponential lower rate. A trial with zero
forcing overlap gives no lower bound at all.

*Proof.* The four-step support in (15) shows that column \(D\) of
\(\mathcal D_3+2I\) is supported in rows \(D-3,\ldots,D\).
The pin adds a separate entry in row zero. Consequently
\[
 (Q^*u)_D=u_0+
       \sum_{j=D-3}^D
              \overline{(\mathcal D_3+2I)_{jD}}\,u_j.
 \tag{68}
\]
Here \(N\ge5\) ensures that row zero is not among those four rows.
The row-sum norms of \(B,Z,L_1\) are at most \(6,6,14\).
Thus (15) gives
\(\|\mathcal D_3+2I\|_\infty
 \le37\cdot14+36+48+8+2=612\).
The four coefficients in (68) have Euclidean norm at most \(1224\).
The reverse triangle inequality and (66) yield
\(\|Q^*u\|_2\ge(1-\varepsilon)|u_0|\), proving (67).
\(\square\)

There is also a precise shifted version. For a trial \(u_h\) in
(61), set \(v=S_hu_h\). Its forcing overlap is
\(|\langle u_h,b_h\rangle|=|v_0|\), while its residual is
\(Q_{3,h}^*u_h=S_{-h}Q^*v\).
If \(v\) satisfies (66), then
\[
 \frac{\sigma_N|\langle u_h,b_h\rangle|}
                         {\|Q_{3,h}^*u_h\|_2}
            \le
       \frac{\sigma_Ne^{\pi D|h|}}{1-\varepsilon},
 \tag{69}
\]
because \(\|S_h\|_2=e^{\pi D|h|}\).
This is a restriction on the stated trials, not on arbitrary
shifted adjoint solutions.

More generally, suppose any independently constructed trial proves
a lower rate \(R>\pi|h|\), in the precise sense that its adjoint
ratio is at least \(e^{NR-o(N)}\). For \(v=S_hu_h\), its
endpoint values must then satisfy
\[
 \left|v_0+\sum_{j=D-3}^{D}
        \overline{(\mathcal D_3+2I)_{jD}}\,v_j\right|
 \le |v_0|e^{-N(R-\pi|h|)+o(N)}.
 \tag{70}
\]
Indeed the left side is at most
\(\|Q^*v\|_2\le e^{\pi D|h|}\|Q_{3,h}^*u_h\|_2\);
substitute the assumed adjoint ratio and
\(\sigma_N=1+O(N^{-2})\).

A positive lower rate above \(\pi|h|\) therefore requires more
than a small bulk annihilation residual for such a construction.
Its transported endpoint values must cancel the pin term in
(68), with the necessary exponential accuracy. Correcting that
single row is not sufficient either: the full residual still
contains the neighboring rows and the rest of the original
recurrence. The cap chart and the exact Gaussian frame make these
quantities computable, but do not supply this cancellation estimate.

### The complete adjoint sweep has no singular pivot

The endpoint issue is not caused by an inability to solve the remaining
rows. For any integer crossing power the canonical sweep can be
completed exactly.

**Proposition 9.** The matrix \(\mathcal D_n\) is upper Hessenberg,
with
\[
 (\mathcal D_n)_{j,j-1}
     =(-1)^{n+1}Q^{nj}\,4\sin^2(\pi j/N)\ne0
           \quad(1\le j<N).
 \tag{71}
\]
Their product is \(\eta N^2\), independently of \(n\).
Starting with \(u_0=1\), solve successively rows \(0,\ldots,D-1\)
of \(Q_n(-2)^*u=0\). Every pivot is nonzero, and the resulting
vector satisfies
\[
       u=\kappa^{-n}Jw_n,\qquad
                Q_n(-2)^*u=\sigma_N\mathbf e_D.
 \tag{72}
\]
Its adjoint lower-bound ratio is exactly one.

*Proof.* The matrix \(M^n\) is lower triangular, including for
negative \(n\), with diagonal \(\mu_j^n\), where
\(\mu_j=\kappa(-1)^jq^{j(j+1)}\).
Conjugating the upper bidiagonal \(Z^{\mathsf T}\) by a lower
triangular matrix gives a lower Hessenberg matrix. Its superdiagonal
entry at \((k,k+1)\) is
\(-4\sin^2(\pi(k+1)/N)(\mu_k/\mu_{k+1})^n\).
Conjugation by \(J\) proves (71), since
\(\mu_{D-j}/\mu_{D-j+1}=-Q^j\).
The sine product is \(N^2\), and
\((-1)^{D(n+1)}Q^{nN(N-1)/2}=\eta\), proving the product claim.

The adjoint of an upper Hessenberg matrix has only one
superdiagonal. In row \(j<D\), its nonzero entry at \(j+1\)
therefore determines \(u_{j+1}\) from the already determined
coordinates. The rank-one pin affects only its last row.
On the other hand \(\kappa^{-n}Jw_n\) has zeroth coordinate
one and, by (61) at \(h=0\), satisfies (72). Uniqueness of
the forward sweep proves the identification. Its forcing overlap
is one and its residual norm is \(\sigma_N\), so the ratio is
\(\sigma_N/\sigma_N=1\). \(\square\)

Thus exact telescoping can cancel every intervening row without
losing the pin, yet still furnish no exponential lower rate.
Moving the residual to a different observation requires additional
control of the corresponding original Green response; nonvanishing
of these pivots does not provide that control.
