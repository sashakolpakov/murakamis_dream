# Moderate bulk interpolation of the actual endpoint value and normal channels

Private written proof, 16 November 2026.

A uniformly analytic matrix recurrence whose step is \(I+O(N^{-1})\)
has an exact holomorphic interpolation on a fixed narrow strip, with
the same polynomial size as its nodal data. A discrete Newton
construction first gives bounded exact local interpolants. Their many
common zeros make the overlap errors exponentially small. A Cauchy
correction and a final sinc repair produce one exact global vector.

For the original microscopic endpoint kernel, the physical value and
common-index normal form such a four-component recurrence. The result
therefore retains both channels without dividing by the value, which
can vanish. It does **not** identify the interpolated normal with the
derivative of the interpolated value. This distinction is essential
for placing the result in the original trace.

## 1. An analytic near-identity recurrence

Let \(I=[a,b]\), \(a<b\), and fix \(R>0\). Write
\[
 \Omega_R=\{z\in\mathbb C:\operatorname{dist}(z,I)<R\},\qquad h=N^{-1}.
\]
Suppose \(T_N\) is a \(d\)-by-\(d\) holomorphic matrix on a neighborhood
of \(\overline{\Omega_R}\), and
\[
                  \|T_N-I_d\|_{\Omega_R}\le A_0h.             \tag{1}
\]
Let vectors \(y_j\) be given at all grid points \(x_j=jh\) in the
real interval \([a-R/2,b+R/2]\), with
\[
 y_{j+1}=T_N(x_j)y_j,\qquad \|y_j\|\le M_N                 \tag{2}
\]
whenever the indicated indices are in this interval. Holomorphic
parameters are permitted, with (1)--(2) uniform on a fixed larger
parameter set.

**Theorem 1.** There are \(r>0\), \(c>0\), \(C<\infty\), and \(N_0\),
depending only on \(I,R,A_0,d\), such that for \(N\ge N_0\) there is a
holomorphic vector \(Y_N\) on
\[
            \mathcal R_r=\{a-r<\Re z<b+r,\ |\Im z|<r\}
\]
with
\[
 Y_N(j/N)=y_j\quad(j/N\in I),\qquad
                         \|Y_N\|_{\mathcal R_r}\le C M_N.     \tag{3}
\]
The construction preserves holomorphic dependence on the parameters.
It consists of bounded exact local Newton polynomials, exponentially
small overlap and gluing errors, and a final correction bounded by
\(CM_Ne^{-cN}\) on this strip. Fixed derivatives have the same bound
\(C_kM_N\) on smaller fixed strips and parameter sets.

One polynomially bounded anchor in (2) suffices to obtain the stated
bound for all its real nodes, after changing a constant. Indeed, for
large \(N\), \(\|T_N\|\le1+A_0h\) and
\(\|T_N^{-1}\|\le1+2A_0h\). There are \(O_I(N)\) steps in the fixed
buffered interval. Forward and backward multiplication therefore
cost a constant independent of \(N\). No eigenvector, logarithm of a
scalar solution, or nonvanishing assumption is involved.

### Exact local Newton polynomials

Here are constants and domains for a proof. Put
\[
 \delta=R/4,\qquad C_0=e(2/\delta+A_0),
\]
and fix
\[
 0<\ell<\min\{R/64,\delta/4,1/(100C_0)\}.                  \tag{4}
\]
We increase \(N_0\) whenever a displayed elementary grid condition is
needed, in particular \(h\le\ell/16\). Local anchors are grid points
in \([a-2\ell,b+2\ell]\), so their closed \(\delta\)-disks lie inside
\(\Omega_R\).

Define matrix functions
\[
 B_0(x)=I_d,\qquad
 B_{k+1}(x)=\frac{B_k(x+h)T_N(x)-B_k(x)}h.                 \tag{5}
\]
For every available string of nodes, induction on \(k\) gives
\[
                        \Delta^k y_j=h^k B_k(x_j)y_j.     \tag{6}
\]
To estimate \(B_k\), use \(k\) nested disks about its anchor, each
losing radius \(\delta/k\). If \(kh\le\delta/2\), a segment of length
\(h\) still leaves Cauchy radius at least \(\delta/(2k)\). Since
\[
 B_{l+1}=\frac{B_l(x+h)-B_l(x)}h
                 +B_l(x+h)\frac{T_N(x)-I_d}{h},
\]
Cauchy's estimate at each step yields
\[
 \|B_k(x_j)\|\le(2k/\delta+A_0)^k
                         \le C_0^k k!.                  \tag{7}
\]
The final inequality uses \(k!\ge(k/e)^k\); the case \(k=0\) is read
separately. The same nested-disk argument applies componentwise in a
fixed matrix norm, or in an operator norm using the vector-valued
Cauchy integral.

Set \(L=\lfloor\ell/h\rfloor\). The Newton polynomial at the anchor
\(x_j\) is
\[
 P_j(z)=\sum_{k=0}^{L}
        \binom{(z-x_j)/h}{k}\Delta^k y_j.                 \tag{8}
\]
It matches the entire string \(y_j,\ldots,y_{j+L}\) exactly. Combining
(6)--(7) with
\[
 h^k k!\left|\binom{(z-x_j)/h}{k}\right|
          =\prod_{v=0}^{k-1}|z-x_j-vh|
          \le(|z-x_j|+\ell)^k
\]
gives
\[
 \|P_j(z)\|\le M_N\sum_{k=0}^{L}
                   [C_0(|z-x_j|+\ell)]^k\le2M_N
                        \quad(|z-x_j|\le8\ell).           \tag{9}
\]
Thus its degree grows with \(N\), but its norm on this fixed disk does
not. Its initial bound uses no cancellation of large coefficients.

### Exponentially small overlaps

Take successive anchors separated by \(J h\), where
\(J=\lfloor L/2\rfloor\). Start with the largest grid point not
exceeding \(a-\ell\), and stop when the last block covers \(b+\ell\).
There are a bounded number of blocks, independent of \(N\), all
within the real buffered interval. The estimates
\[
 Lh\ge15\ell/16,\qquad 13\ell/32\le Jh\le\ell/2             \tag{10}
\]
hold under the preceding grid restriction.

Adjacent polynomials have the common nodes from index \(j+J\) through
\(j+L\). Their number \(K=L-J+1\) is at least \(\ell/(3h)\).
Let \(o\) be the midpoint of this common interval. Every common node
is within \(\ell/3\) of \(o\). Both polynomials are bounded by \(2M_N\)
on the disk \(|z-o|\le6\ell\), since this disk lies inside their
respective disks in (9).

For clarity, the elementary zeros estimate used here is explicit.
An analytic scalar \(f\), bounded by \(M\) on \(|z-o|\le R_1\), with
zeros \(a_\nu\) in that disk, satisfies
\[
 |f(z)|\le M\prod_\nu
 \left|\frac{R_1(z-a_\nu)}
 {R_1^2-\overline{(a_\nu-o)}(z-o)}\right|.                \tag{11}
\]
Divide by the displayed disk Blaschke factors and apply the maximum
principle; their boundary moduli are one and the apparent poles at
the zeros are removable. With \(R_1=6\ell\),
\(|a_\nu-o|\le\ell/3\), and \(|z-o|\le2\ell\), each factor is at most
\(42/106<1/2\). Applied to every component of the difference, this gives
\[
 \|P_{j+J}-P_j\|_{|z-o|\le2\ell}
       \le C_d M_Ne^{-\kappa N},\qquad
                         \kappa=\ell\log2/3.             \tag{12}
\]
All constants are uniform in the holomorphic parameters.

### Global gluing and exact nodal repair

Use real smooth transition functions only in the intervals
\(|\Re z-o|<\ell/8\). These intervals are disjoint by (10); they lie
strictly inside the common-node intervals, whose half-length is at
least \(15\ell/64\). Interpolate from one polynomial to the next with
a fixed smooth function of \((\Re z-o)/\ell\). Outside transitions use
the single appropriate polynomial. This defines a smooth vector
\(F_N\) on
\[
 \mathcal R^{\,0}
 =\{a-\ell/4<\Re z<b+\ell/4,\ |\Im z|<\ell/2\}.
\]
The first and last blocks provide the indicated outer buffers.
Only polynomials whose exact node block contains \(x_j\) are used
at a real grid point \(x_j\in I\). Hence
\[
 F_N(x_j)=y_j,\qquad
 \|F_N\|\le CM_N,\qquad
       \|\bar\partial F_N\|\le CM_Ne^{-\kappa N}.          \tag{13}
\]
The fixed factor \(1/\ell\) is included in \(C\). To check the last
bound, in a transition the derivative is one half the real derivative
of its cutoff times \(P_{j+J}-P_j\). These points lie in the disks of
(12). Away from the transitions that derivative is zero.

Choose a smooth cutoff supported in \(\mathcal R^{\,0}\) and equal to
one on
\[
 \mathcal R^{\,1}
 =\{a-\ell/8<\Re z<b+\ell/8,\ |\Im z|<\ell/4\}.
\]
Extend its product with \(\bar\partial F_N\) by zero, calling the
result \(f_N\). Its plane Cauchy transform
\[
 u_N(z)=\frac1\pi\int_{\mathbb C}
                      \frac{f_N(\zeta)}{z-\zeta}\,dA(\zeta)           \tag{14}
\]
satisfies \(\bar\partial u_N=f_N\). This is the Cauchy--Pompeiu
identity for a smooth compactly supported density. The kernel is
locally integrable and the support lies in a fixed bounded set, so
\[
                         \|u_N\|_{\mathbb C}
                                    \le CM_Ne^{-\kappa N}.          \tag{15}
\]
Thus \(H_N=F_N-u_N\) is holomorphic on \(\mathcal R^{\,1}\), and its
nodal error is precisely \(u_N(x_j)\).

Use \(\operatorname{sinc}(z)=\sin(\pi z)/(\pi z)\), with value one
at zero, and set
\[
 S_N(z)=\sum_{j:\,j/N\in I}u_N(j/N)\operatorname{sinc}(Nz-j),
                       \qquad Y_N=H_N+S_N.                        \tag{16}
\]
This finite sum repairs every node exactly. The integral identity
\(\operatorname{sinc}(z)=\int_{-1/2}^{1/2}e^{2\pi izs}\,ds\) gives
\[
 |S_N(z)|\le CM_N N
                      e^{-\kappa N+\pi N|\Im z|}.                  \tag{17}
\]
Choose
\[
                    r<\min\{\ell/8,\kappa/(4\pi)\}.                \tag{18}
\]
On \(\mathcal R_r\), (17) is at most \(CM_Ne^{-\kappa N/2}\), after
enlarging a constant and \(N_0\). This proves (3). The correction
(14) and (16) is exponentially small relative to \(M_N\); on each
transition the local polynomials already differ by (12).
All operations are linear in the vector data, and the cutoffs and
integration contours do not depend on external parameters.
The integrals therefore preserve their holomorphic dependence.
Cauchy's formula on smaller fixed domains proves the derivative
statement. This completes the proof of Theorem 1.

This construction proves a bounded vector interpolation, not an
exact off-grid solution of the original difference equation. Its
remaining source interpretation must use the exact nodal identities.

## 2. The actual microscopic endpoint system

Use the original data
\[
 \theta=\pi/N,\quad D=N-1,\quad \eta=(-1)^D,\quad
 s_r=2\sin(r\theta),\quad S_j=\prod_{r=1}^j s_r,\quad S_0=1,\quad
 c(r)=2\cos((2r+1)\theta),
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 e_j(z)=S_j^{-2}\prod_{r<j}(c(r)-z),\qquad
 K_N(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w).
                                                                    \tag{19}
\]
Fix \(0<a<b<1/2\), \(I=[a,b]\), and any bounded complex parameter
disk \(|\alpha|\le A\). Put
\[
 w_N(\alpha)=2\cosh(\alpha/N),\quad
 F_j(\alpha)=K_N(c(j),w_N(\alpha)),\quad
 G_j(\alpha)=\partial_zK_N(c(j),w_N(\alpha)).
\]
The parameter disk may be enlarged whenever fixed parameter
derivatives are wanted.

The original difference coefficients are
\[
 A_N(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C_N(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},\qquad
                         c'(r)=-4\theta\sin((2r+1)\theta).          \tag{20}
\]
The subscript distinguishes the coefficient \(A_N\) from the bound
on \(\alpha\). The literal off-grid source identity is
\[
 \begin{split}
 A_N(r)K_N(c(r+1),w)
  ={}&(c(0)+A_N(r)+C_N(r)-w)K_N(c(r),w)\\
    &-C_N(r)K_N(c(r-1),w)
                  +\frac{\eta P_N(w)}{N^2}e_D(c(r)).
 \end{split}                                                       \tag{21}
\]
This is the full polynomial identity, before specialization or
differentiation. At every bulk physical index \(j\ge1\) under
consideration, \(e_D(c(j))=e_D'(c(j))=0\): the corresponding spectral
root occurs twice in \(e_D\). Therefore the source in (21) and its
common-index derivative both vanish there. They have not been
discarded at \(j=0\) or away from the physical grid.

Define, for \(x=r/N\),
\[
 q_N(x)=C_N(Nx)/A_N(Nx),\qquad
 d_N(x)=\frac{c(0)-w_N(\alpha)}{A_N(Nx)},\qquad
 T_N(x)=
 \begin{pmatrix}
 1+d_N(x)&q_N(x)/N\\
 Nd_N(x)&q_N(x)
 \end{pmatrix}.                                                   \tag{22}
\]
The exact value vector and its scaled common-index normal are
\[
 X_j=\binom{F_j}{N(F_j-F_{j-1})},\qquad U_j=c'(j)G_j,\qquad
 Y_j=\binom{NU_j}{N^2(U_j-U_{j-1})}.                               \tag{23}
\]
Equation (21) and its derivative give exactly
\[
 X_{j+1}=T_N(j/N)X_j,\qquad
 Y_{j+1}=T_N(j/N)Y_j+(\partial_xT_N)(j/N)X_j.                       \tag{24}
\]
For the derivative equation, \(Y_j\) is \(N\) times the common-index
derivative of the displayed off-grid value vector. The chain rule
for \(T_N(r/N)\) supplies \(\partial_xT_N\), with no missing factor
of \(N\). All terms involving the endpoint source vanish only for
the bulk indices just specified.

Consequently \(Z_j=(X_j,Y_j)^T\) obeys the exact four-component
recurrence
\[
 Z_{j+1}=\mathbb T_N(j/N)Z_j,\qquad
 \mathbb T_N(x)=
 \begin{pmatrix}T_N(x)&0\\ \partial_xT_N(x)&T_N(x)\end{pmatrix}.
                                                                    \tag{25}
\]
Choose a fixed sufficiently small \(R>0\) such that the closure of
\(\Omega_R\) stays away from \(0\) and \(1/2\), and from the zero sets
of their sine and cosine denominators. On a slightly larger such
domain, uniformly for bounded complex \(\alpha\),
\[
 A_N(Nx)=\tan^2(\pi x)+O(N^{-1}),\quad
 q_N(x)=1+O(N^{-1}),\quad d_N(x)=O(N^{-2}).                          \tag{26}
\]
Here \(c(0)-w_N(\alpha)=-(\pi^2+\alpha^2)N^{-2}+O(N^{-4})\);
the limiting \(A_N\) is a unit. Direct holomorphic substitution in
(20), followed by Cauchy estimates on the larger domain, proves
(26) with all fixed \(x\)-derivatives. In particular
\[
                 \mathbb T_N=I_4+O(N^{-1})                        \tag{27}
\]
uniformly and holomorphically. No scalar root of a characteristic
equation or of \(F_j\) is used.

## 3. Polynomial initial size and exact two-channel interpolation

The pinned endpoint-product theorem, with one factor, gives
\[
 \sup_{z\in[-2,2],\ |\alpha|\le A}
                 |K_N(z,w_N(\alpha))|\le C_A N^{p_A}.              \tag{28}
\]
It holds on every bounded complex parameter disk, not only below
the first endpoint zero. Its proof compares the physical values to
one fixed low physical row and retains the whole high radical.
Markov's inequality for the ordinary degree-\(D\) kernel gives
\[
               |G_j(\alpha)|\le C_A N^{p_A+2}.                    \tag{29}
\]
Since \(|c'(j)|\le4\pi/N\), (23) yields the sufficient bound
\[
                            \|Z_j\|\le C_A N^{p_A+3}              \tag{30}
\]
on the entire buffered bulk node interval. Differences in (23) are
bounded by the sum of their two actual endpoint norms; no smoothness
of the unknown interpolation is assumed.

Apply Theorem 1 to (25). Denote its first and third components by
\(\mathcal F_N(x,\alpha)\) and \(\mathcal U_N(x,\alpha)\).
Shrinking its fixed strip if necessary, define
\[
 \mathcal G_N(x,\alpha)=
       \frac{\mathcal U_N(x,\alpha)}{N c'(Nx)}
       =-\frac{\mathcal U_N(x,\alpha)}
                     {4\pi\sin(2\pi x+\pi/N)}.                    \tag{31}
\]
The denominator is bounded away from zero on this bulk strip.
Thus for some fixed \(r>0,C,p\), at both parities and all sufficiently
large \(N\),
\[
 \boxed{\quad
 \mathcal F_N(j/N,\alpha)=F_j(\alpha),\qquad
 \mathcal G_N(j/N,\alpha)=G_j(\alpha),\qquad
 \|\mathcal F_N\|+\|\mathcal G_N\|\le CN^p
 \quad}                                                         \tag{32}
\]
on \(\mathcal R_r\), uniformly for \(|\alpha|\le A\).
Both interpolants are jointly holomorphic. All fixed index-strip
and exterior-parameter derivatives have polynomial bounds on
smaller fixed domains. The other two vector components interpolate
the differences in (23) and remain available.

This is a phase-free analytic interpolation of both **separate**
physical channels: its norm has no extensive exponential rate.
No scalar zero-freeness or separation of limiting modes is needed.
Any \(N\)-dependent oscillation in the actual vector initial data
is retained rather than normalized away.

## 4. Original trace placement and its precise limitation

For any actual ordinary spectator \(f(z;\mathbf u)\), the contribution
of the bulk rows \(J_I=\{j:j/N\in I\}\) to the original full trace is
exactly
\[
 \eta\sum_{j\in J_I}
 \left[
 (4-c(j)^2)
 \{G_j(\alpha)f(c(j);\mathbf u)
              +F_j(\alpha)\partial_z f(c(j);\mathbf u)\}
       -c(j)F_j(\alpha)f(c(j);\mathbf u)
 \right].                                                       \tag{33}
\]
Any original crossing \(R^n\), including its carrier and normal,
can remain inside \(f\). Every other graph factor and remaining
trace can remain jointly inside \(f\) as well. The replacements
\(F_j\mapsto\mathcal F_N(j/N,\alpha)\) and
\(G_j\mapsto\mathcal G_N(j/N,\alpha)\) leave (33) exactly unchanged.
All ordinary exterior derivatives commute with these identities.

For fixed shared endpoint products, their value and normal in (33)
are respectively
\[
 \prod_i\mathcal F_N(x,\alpha_i),\qquad
 \sum_i\mathcal G_N(x,\alpha_i)
                         \prod_{k\ne i}\mathcal F_N(x,\alpha_k).   \tag{34}
\]
These have polynomial bounds on the common strip and reproduce the
entire shared product rule. No quotient is imposed on a free outside
variable, and no spectral normal of the spectator is removed.

The theorem does not assert
\[
            \partial_x\mathcal F_N(x,\alpha)
                  =N c'(Nx)\mathcal G_N(x,\alpha).                \tag{35}
\]
Interpolating the two components separately is sufficient for the
two-channel sampling formula (33), but does not create a single
scalar Hermite representative. Accordingly (32) alone does not
justify replacing a scalar double-pole contour amplitude by
\(\mathcal F_N\) and differentiating it. Such a replacement must
retain the difference between the two sides of (35), with its
actual current or normal contribution.

The physical endpoints \(j/N=0,1/2\) are outside the fixed bulk
hypothesis. The odd simple node is therefore not among (33);
its separate original value remains untouched. Both even and odd
bulk recurrences are covered by the same argument. No global
periodicity, endpoint connector estimate, filled-action upper
bound, or nonzero source coefficient follows from this result.
In particular it does not contradict the full-period scalar
Hermite obstruction.

## 5. Coverage and direct sources

The original physical value recurrence and its differentiated
source equation are archived. The endpoint polynomial bound is
also prior. The added result is the analytic near-identity vector
interpolation theorem, and its application to the actual coupled
value/normal data, including all shared endpoint products.

Both complete direct sources were read at the following versions,
their directly used implications checked, and their hashes verified:

* [All physical first normals](research_all_color_path_normal_bound.md),
  SHA256 08f8932c2cdee4c7afadbb4db3cd85480603f8adb4c936ce29a5517b2d4799c7:
  the original source difference equation, common-index
  differentiation, endpoint forcing, and full-normal conventions.
* [Two half-plane endpoint-product representatives](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  the actual polynomial bound for every bounded complex microscopic
  parameter set and the original full-normal trace normalization.

Only written mathematics, source-text reads, and file hashes were
used. No mathematical program, numerical experiment, test, or build
was run. Adopted files and public manuscripts remain unchanged.

