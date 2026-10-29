# A complete positive Fourier--Hermite filling Gram and an actual source discriminant

29 October 2026. The full crossing-circle kernel gives an explicit
positive, full-rank coherent Gram, independent of the unknown period.
Its filling-source dual norm is exactly
1+ell^2(N^2-1)/(12N^2). It retains every confluent Casimir jet.
The same construction has a precise limitation: its energy is
polynomially equivalent to the whole mixed-color packet energy,
so it does not automatically see the smaller filled volume.

## 1. Complete data and the positive metric

Use the ORIGINAL kernel and conventions of
[the Fourier--Hermite theorem](actual_twist_circle_fourier_kernel.md).
For an integer crossing power ell let h_k=nu_k^ell,
d_k=-ell(d-2k)h_k/2, w_k=q^(2k+1), d=N-1. Put

\[
 H_n=N^{-1}\sum_kh_kw_k^{-n},\qquad
 D_n=N^{-1}\sum_kd_kw_k^{-n}.
\]

Their exact marked aliases are H_(N-n)=-H_n, D_(N-n)=D_n,
D0=0. For n<N/2 write m=N-n and r=n/N. Define N orthonormal
compatible-data coordinates

\[
 y_0=H_0,\qquad (y_{n,H},y_{n,D})=(\sqrt2H_n,\sqrt2D_n/N),
\]

with the additional y_mid=D_(N/2)/N when N is even. At that index
H_(N/2)=0. Odd N has no middle coordinate; its simple Casimir node
has only a value, with logarithmic derivative zero automatically.

Let a be the first-kind Chebyshev coefficient vector. The exact
alias inverse a=K y is

\[
 a_0=y_0,\qquad
 \begin{pmatrix}a_n\\a_m\end{pmatrix}
 =\frac1{\sqrt2}\begin{pmatrix}1-r&1\\-r&1\end{pmatrix}
              \begin{pmatrix}y_{n,H}\\y_{n,D}\end{pmatrix},
 \qquad a_{N/2}=y_{\rm mid}.                              \tag{1}
\]

Define the real difference matrix S by
\(\beta_j=(-1)^j(a_j-a_{j+2})\), with a_N=a_(N+1)=0, and set
B=S K. The original all-input filling identity is

\[
 R^{\ell}=\kappa^{\ell}\sum_{j=0}^d\beta_jL_{j+1},
 \qquad\beta=B y.                                         \tag{2}
\]

Every L_(j+1) is the literal ordinary auxiliary-circle operator,
with its full Cartan and pivot and no added color average, by
[the original circle-source proof](actual_crossing_circle_source_and_filling.md).

For a complete mixed-color exterior packet A=(A0,...,Ad)^T put
z=B^T A and

\[
 \boxed{\quad E_N(A)=\|z\|^2=A^\dagger G_N A,
                  \qquad G_N=\overline B B^{\mathsf T}>0.\quad} \tag{3}
\]

B is real in these coordinates, but the conjugation in (3) makes
the complex Riesz convention explicit. There is a particularly
simple direct formula. Set eta_n=(-1)^n(A_n-A_(n-2)), A_negative=0.
Then z0=eta0, and for n<m,

\[
 z_{n,H}=((1-r)\eta_n-r\eta_m)/\sqrt2,\qquad
 z_{n,D}=(\eta_n+\eta_m)/\sqrt2,
\]

with z_mid=eta_mid when present. Thus the energy keeps explicit
cross-color interference, not just separate squared color values.

Marked Fourier Parseval gives the EXACT source cost

\[
 \boxed{\displaystyle
 \|y_\ell\|^2=\frac1N\sum_k(|h_k|^2+|d_k/N|^2)
           =1+\frac{\ell^2(N^2-1)}{12N^2}=:c_{N,\ell}.}     \tag{4}
\]

Here sum_k(d-2k)^2=N(N^2-1)/3. Since B is invertible, this is
also the exact dual norm
beta^T G_N^(-1) conjugate(beta), not just an upper bound.
For the original scalar, with its actual external line chi retained,

\[
 |\chi\kappa^{\ell}\beta^{\mathsf T}A|^2
                    \leq|\chi|^2c_{N,\ell}E_N(A).           \tag{5}
\]

The pairing is y^T z; its Hilbert Riesz vector is conjugate(y).
No unknown closed invariant defines the metric.

Equations (3)--(5) also apply to Hilbert-valued packets. For arbitrary
operator-valued exteriors A_j, preserving their original order, they
give the all-input positive inequality

\[
 (\sum_j\beta_jA_j)^\dagger(\sum_j\beta_jA_j)
                         \preceq c_{N,\ell}\sum_r Z_r^\dagger Z_r. \tag{6}
\]

All original Casimir jets are retained. This is a genuine positive
filling port, not an inverse of the possibly nilpotent complete-color
circle alone.

## 2. Polynomial conditioning and simultaneous fillings

Each two-by-two block in (1) has norm at most sqrt(3/2) and inverse
norm at most sqrt6. Also ||S||<=2 and ||S^(-1)||<=N, by finite
summation along each parity chain. Therefore

\[
 \boxed{\displaystyle
 (6N^2)^{-1}\|A\|^2\leq E_N(A)\leq6\|A\|^2,
                       \qquad\operatorname{cond}(G_N)\leq36N^2.} \tag{7}
\]

For s specified twist boxes use the tensor product transform B^T
on the s color registers, AFTER retaining their entire original
mixed-color exterior. The dual cost is exactly
product_i c_(N,ell_i), and the Gram is positive full rank with
polynomial conditioning for fixed s. Physical boxes may overlap
in time; the original operator order in each packet entry is not
changed. This does not assume independent physical contractions.

For full twists ell_i=2p_i, the cost is at most product_i(1+p_i^2/3),
independent of N. It is subexponential whenever
sum_i log(1+|p_i|)=o(N). All source, framing, and peripheral factors
remain the exact ones outside the filling identity (2).

## 3. A complete actual source discriminant

Use the original four-plat multiplicities, cup p, cap ell and full
crossings R1,R2 from the source theorems. Define ONE fixed base packet

\[
 A_j=\ell R_2^2L_{j+1}(\Omega_{12})R_1R_2p,\quad0\leq j<N.
\]

The raw filled period with slope p is
F_p=ell R2^2 R1^(2p+1) R2 p=kappa^(2p) beta_(2p)^T A.
The original normalization/cup slide and whole figure-eight source
give the EXACT values

\[
 F_0=A_0=x^d=\kappa^2,\qquad
 F_{-1}=Z_N:=\sum_{a=0}^d|(Q;Q)_a|^2.                      \tag{8}
\]

No augmented geometric saddle is assumed. The second value is the
literal original [figure-eight whole-source identity](figure_eight_whole_source_identity.md);
the first is the actual [all-input normalization tangle](actual_terminal_source_normalization_packet.md).
Apply (5) with ell=-2. Since c_(N,-2)<=4/3,

\[
 \boxed{\displaystyle E_N(A)\geq\frac34 Z_N^2.}              \tag{9}
\]

At p=0 the exact dual cost is 1 and the filled raw scalar has modulus
one, yet the SAME coherent positive energy has positive exponential
rate. This is a fully contracted original packet, not an expanded
absolute-value path or a guessed augmented invariant.

It also quantifies the requirement on a different color metric H.
The bound ||B||^2<=6 and (4) give ||beta_(-2)||^2<=8. Hence
||A||^2>=Z_N^2/8. The p=0 source is beta0=e0, so its Cauchy budget
under ANY positive H satisfies

\[
 (A^\dagger H A)(e_0^\dagger H^{-1}e_0)
                  \geq Z_N^2/[8\operatorname{cond}(H)].      \tag{10}
\]

A zero-exponent sharp budget for this normalization therefore requires
exponential metric anisotropy, or actual coherent pruning before the
energy is formed. Polynomial-conditioned changes of the complete
Fourier--Hermite norm cannot supply it. Exponential anisotropy is
allowed; (10) is a necessary quantitative condition, not a no-go
theorem for all coherent metrics.

## 4. The same defect persists in a hyperbolic final knot

There is a source-exact all-width insertion, not merely a scalar
coincidence. Let M_j be the physical one-input/one-output tangle
whose complete source entry is A_j. Each crossing, original turn,
and auxiliary pivotal loop is a Hopf map. Thus M_j commutes with K
and F on the original complete V_N. Its K eigenvalues are distinct,
so it is diagonal; every interior F coefficient is nonzero, so all
diagonal entries agree. Consequently M_j=A_j I at EVERY N.

The p=0 tangle is topologically the straight unframed strand. Here
is the local move proof, separately from its scalar evaluation:
slide the free strand past the neighboring cup (the oriented cup-slide
Reidemeister-II isotopy), leaving the two crossings directly above
that cup. Each is a removable Reidemeister-I kink on the same arc.
The remaining cup/cap cancels by the snake isotopy. No closed
component remains. In the actual framed tensor calculation the two
kinks have the retained unit factor kappa^2, as (8) verifies on every
input; the prescribed zero-framing line is kept when this tangle is
inserted into a diagram.

Insert it into a strand of any original knot J. The raw mixed-color
packet is multiplied by its original cut scalar, and after retaining
the original external line its energy is |K_N(J)|^2 E_N(A), up to
the displayed unit framing phase. All such phases remain in the
exact scalar identity and do not change this norm. The unframed
p=0 filled knot is still J. By (9),

\[
 E_N^{\rm inserted}(J)\geq\frac34|K_N(J)|^2 Z_N^2.           \tag{11}
\]

For the independently proved benchmark J=4_1, K_N(J)=Z_N, so this
Gram has energy at least 3Z_N^4/4 while the final knot has squared
scalar Z_N^2. Its energy exponent is at least DOUBLE the correct
figure-eight squared-volume exponent.

This counterexample uses a redundant normalization augmentation and
the p=0 filling. It does NOT exclude a properly reduced fully augmented
diagram or a long-filling subclass. It proves that exact filling,
complete jets, and a polynomial dual source cost do not by themselves
imply the filled-volume energy bound. Normalization pruning or a
source/slope-dependent geometric norm remains substantive.

[Audit](../experiments/audit_actual_filling_fourier_hermite_gram.py)
checks the full marked aliases and positive Gram, exact source dual
costs, all-input operator inequality, original mixed-color scalar
tangles, and the two actual source fillings (8). No geometric energy
bound is inferred from interpolation or from coefficient mass.

Fresh replay: PASS seven complete positive Grams with49 signed
dual-source costs; five literal all-input mixed-circle packets
N=2,...,6; six complete original two-filling energy discriminants.
