# Recovering the source from its charge period increment

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The physical values of the original charged edge determine its first
normals through the existing Jacobi formula. Here we use that formula
to reconstruct the original charge observations from their finite
period increment. The reconstruction has polynomial norm, keeps the
odd simple node, and retains the derivative of every charge coupon.
It does not give a lower bound for one Fourier coefficient.
The relative normal bound and coercivity are existing inputs:
the [tree normal theorem](research_all_color_path_normal_bound.md#5-the-complete-normal-determinant-at-every-color-assignment)
already proves the stronger statement for every original
color assignment on a tree. The additional calculation here
is the bounded reconstruction from the period increment,
including the simple node that this increment cannot see.

## 1. The relative normal formula already proved

Use the original algebra, Newton basis, turn, and trace:
\[
 \begin{gathered}
 \theta=\pi/N,\quad D=N-1,\quad\eta=(-1)^D,\quad
 s_r=2\sin(r\theta),\quad c_j=2\cos((2j+1)\theta),\\
 P_N(z)=2T_N(z/2)+2,\quad
 e_j(z)=\frac{\prod_{r<j}(c_r-z)}{\prod_{r=1}^j s_r^2},
 \quad K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w),\\
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
 \end{gathered}
 \tag{1}
\]
Fix an integer \(n\) and \(w\in[-2,c_0]\). Let
\[
 f(z)=R(z)^nK_N(z,w),\qquad
 Z_k=\phi_N(fT_k(-z/2)),\qquad
                       \Delta_k=Z_{k+N}-\eta Z_k .
 \tag{2}
\]
All crossing phases and signed powers are the original ones.
The distinct double roots have indices
\(0\le j\le\lfloor(N-2)/2\rfloor\). Put
\[
 \tau_j=\pi-(2j+1)\theta>0,\quad
 F_j(w)=K_N(c_j,w),\quad G_j(w)=\partial_zK_N(c_j,w),
 \quad u_j(w)=G_j(w)/F_j(w),\quad Q(w)=G_0(w).
 \tag{3}
\]
The [all-color normal theorem, Lemma 5](research_all_color_path_normal_bound.md#5-the-complete-normal-determinant-at-every-color-assignment)
already proves \(F_j(w)\ge1\), \(u_j(w)\in\mathbb R\), and
\[
                         |u_j(w)|\le N^{11}.
 \tag{4}
\]
Its exact formula, including the free-boundary source, is
\[
 \begin{split}
 c'(j)u_j(w)={}&c'(0)Q(w)
  +\operatorname{Tr}((J_j-wI)^{-1}J_j')
       -\sum_{r=0}^{j-1}A'(r)/A(r)\\
 &+\frac{c'(0)P_N(w)}{N^2s_1^2}
                         ((J_j-wI)^{-1})_{00},
 \qquad c'(j)=-4\theta\sin((2j+1)\theta).
 \end{split}
 \tag{5}
\]
At \(j=0\), use \(u_0=Q\). Here
\[
 A(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},\quad C(0)=0,
 \tag{6}
\]
and \(J_j\) is the symmetric \(j\)-row Jacobi matrix with
diagonal \(c_0+A(r)+C(r)\) and off-diagonal
\(-\sqrt{A(r)C(r+1)}\). Primes in (5) are the common
index shift used in that theorem.
Thus (5) uses only the positive finite Jacobi matrices and
the original endpoint polynomial \(Q\), not the unknown
trace \(Z_0\). The existing proof gives
\(J_j-c_0I\ge16N^{-5}I\), the full endpoint bound
\(|Q(w)|\le N^4/4\), and (4).
The term \(P_N(w)\) in (5) must be retained; at \(w=-2\)
it is nonzero at even levels.

## 2. Inverting the value observation, including the odd endpoint

Use all \(N\) angular samples
\(\tau_a=\pi(D-2a)/N\). The
[full derivative-sampling identity](research_fourier_lower_bounds_and_almost_invariance.md#15-the-exact-finite-system-for-changing-a-fourier-charge)
gives exactly
\[
 \Delta_k=-iN\sum_{a=0}^{N-1}e^{-ik\tau_a}
                         \sin\tau_a\,f(c_a).
 \tag{7}
\]
Consequently every double-node value is recovered by
\[
 v_j:=f(c_j)
       =\frac{i}{N^2\sin\tau_j}
                  \sum_{k=0}^{N-1}\Delta_k e^{ik\tau_j}.
 \tag{8}
\]
No first normal has been estimated or omitted in deriving (7).
It is their exact period difference.

For even \(N\), (8) recovers every distinct physical value.
For odd \(N=2m+1\), the simple node is \(-2\), with
\(\tau_m=0\), so it is invisible to (7). It is recovered
from the last ordinary Jacobi row. Write
\(r_j=R(c_j)^n\), including \(r_m=R(-2)^n\), and
put \(r=m-1\). Then
\[
 f(-2)=r_m\left\{
   \frac{c_0+A(r)+C(r)-w}{A(r)}
                       \frac{v_{m-1}}{r_{m-1}}
  -\frac{C(r)}{A(r)}\frac{v_{m-2}}{r_{m-2}}\right\}.
 \tag{9}
\]
When \(m=1\), the last term is absent since \(C(0)=0\).
The equation is the original value recurrence
\(A(r)F_{r+1}=(c_0+A(r)+C(r)-w)F_r-C(r)F_{r-1}\).
All \(r_j\) have modulus one.

This last step has a uniform bound. Indeed
\[
 A(m-1)\ge9/4,\quad
 0\le C(m-1)/A(m-1)\le1,\quad
 0<\frac{c_0+A(m-1)+C(m-1)-w}{A(m-1)}<4 .
 \tag{10}
\]
For the first inequality use
\(s_m=2\cos(\theta/2)\ge\sqrt3\).
For \(m\ge2\), the second follows from
\[
 C(m-1)/A(m-1)
      =(s_{m-1}/s_m)^4\,s_1/s_3\le1 .
 \tag{11}
\]
The case \(m=1\) is zero. The last inequality in (10)
uses \(c_0-w\le4\).

The finite Fourier transform in (7) is unitary after division
by \(\sqrt N\), and \(\sin\tau_j\ge2/N\) at every double
node. Thus the reconstructed distinct double-node vector has
norm at most \(\|\Delta\|_2/(2\sqrt N)\). Adding (9)
gives the convenient common bound
\[
              \|v_{\rm all}\|_2\le3N^{-1/2}\|\Delta\|_2 .
 \tag{12}
\]
Here \(v_{\rm all}\) lists distinct physical values, with the
simple value included only at odd levels.

## 3. The normal lift and the full charge formula

The original Gaussian crossing jets give
\[
 f'(c_j)=\{u_j(w)+in\gamma_j\}v_j,\qquad
 \gamma_j=\frac{N\tau_j}{4\pi\sin\tau_j},
                    \qquad 0<\gamma_j\le N^2/8 .
 \tag{13}
\]
The original full residue trace is
\[
 \phi_N(f)=
 \eta\sum_{\text{double }j}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
                 +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{14}
\]
Define
\[
 a_j=(4-c_j^2)u_j-c_j,\qquad
 b_j=(4-c_j^2)\gamma_j
                =N\tau_j\sin\tau_j/\pi .
 \tag{15}
\]
These are real and obey
\[
                 |a_j|\le6N^{11},\qquad 2/N\le b_j\le N .
 \tag{16}
\]
The exact charge observation is therefore
\[
 \begin{split}
 Z_k={}&\eta\sum_{\text{double }j}v_j
   \{(a_j+inb_j)\cos(k\tau_j)
                    -2k\sin\tau_j\sin(k\tau_j)\}\\
 &+\mathbf1_{N\ {\rm odd}}f(-2).
 \end{split}
 \tag{17}
\]
The sine term is the derivative of the coupon. It is present
also when its cosine value vanishes. The odd simple node has
only its value contribution.

**Proposition 1.** Equations (5), (8), (9), and (17) give
an explicit linear reconstruction
\[
 \mathcal R_{n,N,w}(\Delta_0,\ldots,\Delta_{N-1})
                         =(Z_0,\ldots,Z_{N-1})
 \tag{18}
\]
on the original endpoint-supported source line. Its entries
do not involve any of the unknown \(Z_k\), and
\[
                    \|\mathcal R_{n,N,w}\|
                        \le3(8+|n|)N^{12}
                         \quad(-2\le w\le c_0).
 \tag{19}
\]
It also applies to any scalar multiple of that source.

*Proof.* Fourier inversion proves (8), the original value
equation proves (9), and the known full normal formula proves
(13). Substitution into the trace of the product with the
coupon proves (17). For \(0\le k<N\), each coefficient
in braces has modulus at most \((8+|n|)N^{11}\).
Cauchy--Schwarz, the number of distinct nodes being at most
\(N\), and (12) give a bound
\(3(8+|n|)N^{11}\|\Delta\|_2\) for each output.
Taking the output norm proves (19), with room to spare.
\(\square\)

The source-line qualification is essential. For \(N\ge4\), the extra channel
in the [two-channel equation](research_current_free_aw_crossing_transport.md#12-the-physical-charge-equation-has-two-channels)
is radical and has zero increment \(\Delta\), but can have
nonzero trace. Its normals are not the source normals (13).
Thus (18) does not reconstruct arbitrary Hermite data from
their values.

There is a useful coercivity in this lift, distinct from the
Fourier observation. For \(n\ne0\), the double-row diagonal
map \(\mathsf A=\operatorname{diag}(a_j+inb_j)\) satisfies
\[
 \operatorname{sgn}(n)\Im\langle x,\mathsf Ax\rangle
       \ge\frac{2|n|}{N}\|x\|_2^2,\qquad
                    \|\mathsf A^{-1}\|\le\frac{N}{2|n|}.
 \tag{20}
\]
This is a direct consequence of (16), and is the
one-vertex form of the already proved normal accretivity.
At odd levels append the simple coefficient one; rotate
the double block by \(-i\operatorname{sgn}(n)\) while
leaving that simple block unchanged. The real part is
then bounded below by \(\min(1,2|n|/N)\).

## 4. The remaining projection

The physical normal reconstruction costs only powers of \(N\).
The unresolved exponential estimate is the Fourier projection
in (17). Its summands still have the exact quadratic phases
\(R(c_j)^n\). The coercive form (20) pairs a vector with
itself; the original trace sums its components. These are
different operations.

In particular (19) is an upper bound for a reconstruction
operator, not a lower bound for its central row on the source.
The already proved small-charge Gaussian packet supplies
a local nonzero observation, but the argument here does
not transport its coefficient to charge one.

All uniform bounds used above concern real \(w\in[-2,c_0]\).
They do not extend the canonical endpoint normal with the
same bound to a fixed complex strip. The
[logarithmic-factorial representative](research_odd_ward_logarithmic_factorial.md)
has its separately proved meaning inside an original
contraction, with its endpoints retained.

The [finite reconstruction checker](../experiments/check_physical_normal_lift.py)
computes the charge observations from the original Newton
crossing matrices, then reconstructs them by (8), (9), and
(17). The normals in that reconstruction are obtained from
the independent shifted-row identity, with its free \(P_N(w)\)
term retained. The
[100-digit record](../repro/results/research-physical-normal-lift.json)
checks signed and zero powers, both level parities, the
complete free color, and the odd simple-node recovery.
These comparisons check the finite normalization; the
uniform operator bound is the written proof of Proposition 1.
