# A reflection-symmetric geometric path and an orthogonal boundary frame

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

Damp an angle \(x\) by \(r^{\min(x,1-x)}\). This preserves the
growing geometric contribution of both the trivalent source and the
crossing kernel, while treating complementary angles symmetrically.
The resulting complete sampling frame has a positive polar
orthogonalization which preserves both the original Hermitian norm
and the anti-diagonal Frobenius pairing exactly.

The geometric estimates apply to the raw samples. Orthogonalization
is an explicitly retained matrix operation; it does not automatically
transfer a particular entry's asymptotic or prove that a final knot
closing is nonzero.

## 1. A growing path invariant under angle reflection

For \(0<x<1\), put
\[
             w(x)=\min(x,1-x),\qquad
             t(x,r)=-r^{w(x)}e^{-2\pi ix},\quad 0<r\le1.
 \tag{1}
\]
Thus \(w(1-x)=w(x)\). Use the original initialized actions
\[
 \begin{split}
 \Psi(\mathbf t)={}&-\frac{\pi}{12}
 +\frac{\sum_i\operatorname{Li}_2(-t_i)
        +\operatorname{Li}_2(-t_1t_2t_3)
        -\sum_{i<j}\operatorname{Li}_2(t_it_j)}{2\pi},\\
 \Psi_0(y,z)={}&-\frac{\pi}{12}
 +\frac{\operatorname{Li}_2(-y)+\operatorname{Li}_2(-z)
                         -\operatorname{Li}_2(yz)}{2\pi}.
 \end{split}
 \tag{2}
\]
Their branches start from the disk power series.

**Theorem 1.** The path (1) has positive height
\(-\operatorname{Im}\Psi>0\) for every strict prism
\[
 x_i>0,\quad x_i+x_j<1\ (i\ne j),\quad S:=x_1+x_2+x_3>1,
 \tag{3}
\]
and positive height \(-\operatorname{Im}\Psi_0>0\) for every
strict tetrahedron \(b,c>0,\ b+c<1\), using its two parameters
\(t(b,r),t(c,r)\). Both assertions are uniform on strict angle
compacts and \(r\in[r_0,1]\), for fixed \(r_0>0\).

We prove the height assertions directly. Write
\[
F_\rho(u)=-\operatorname{Im}\operatorname{Li}_2
                   (\rho e^{-2\pi iu}),\qquad 0<\rho\le1.
 \tag{4}
\]
On \(0<u<1/2\), this is positive and strictly concave in \(u\),
increasing in \(\rho\), and convex in \(\log\rho\). Indeed
\[
 \partial_u^2F_\rho=
 -\frac{4\pi^2\rho\sin2\pi u}{1-2\rho\cos2\pi u+\rho^2}<0,\qquad
 \partial_{\log\rho}F_\rho=\arg(1-\rho e^{-2\pi iu})>0,
 \quad
 \partial_{\log\rho}^2F_\rho=
 \frac{\rho\sin2\pi u}{1-2\rho\cos2\pi u+\rho^2}>0.
 \tag{5}
\]
Also \(F_\rho(0)=F_\rho(1/2)=0\) and
\(F_\rho(1-u)=-F_\rho(u)\). The formulas extend continuously
to \(\rho=1\) on this open angle interval.

For a tetrahedron with \(b,c\le1/2\), the height is positive
for arbitrary positive radii: if \(b+c\ge1/2\) the subtracted
pair has favorable sign; otherwise strict angle subadditivity
and radius monotonicity give
\[
 F_{\rho\sigma}(b+c)<
       F_{\rho\sigma}(b)+F_{\rho\sigma}(c)
                         \le F_\rho(b)+F_\sigma(c).
 \tag{6}
\]
If \(b=1-\delta>1/2\), then \(0<c<\delta<1/2\).
The folded height, multiplied by \(2\pi\), is
\[
                -F_{r^\delta}(\delta)
                   +F_{r^c}(c)+F_{r^{\delta+c}}(\delta-c).
 \tag{7}
\]
Set \(f(e)=F_{r^e}(\delta)\), a convex function of \(e>0\).
Strict angle concavity gives the strict lower bound
\[
   -f(\delta)+\frac c\delta f(c)
                         +\frac{\delta-c}{\delta}f(\delta+c)
                         \ge0.
 \tag{8}
\]
The last step is Jensen's inequality, since the weighted
exponent is \(\delta\). The preceding angle inequality is
strict, including at \(r=1\). The other large-angle case is
symmetric.

For the prism, if all \(x_i\le1/2\), all pair angles exceed
\(1/2\) and the triple angle \(S-1\) lies in \((0,1/2)\);
the height is positive term by term. Otherwise write
\[
 a=x_1=1-\delta>1/2,\quad b=x_2,\quad c=x_3,\quad
 s=b+c,\quad u=s-\delta,\quad p=\delta-b,\quad q=\delta-c.
 \tag{9}
\]
Then \(0<u<b,c<\delta<1/2\), \(p,q>0\), and
\[
             b=u+q,\quad c=u+p,\quad
             \delta=u+p+q,\quad s=2u+p+q.
 \tag{10}
\]
The full reflected height is
\[
 \begin{split}
 -2\pi\operatorname{Im}\Psi={}&
 F_{r^b}(b)+F_{r^c}(c)-F_{r^\delta}(\delta)
       +F_{r^{\delta+s}}(u)\\
 &+F_{r^{\delta+b}}(p)+F_{r^{\delta+c}}(q)-F_{r^s}(s).
 \end{split}
 \tag{11}
\]
When \(s\ge1/2\), its last term is favorable. The first
three terms are strictly positive: monotonicity replaces
the first two radii by \(r^\delta\), and strict concavity
uses \(b+c=\delta+u\). This settles that case.

If \(s<1/2\), again set \(f(e)=F_{r^e}(\delta)\).
The positive angle weights and radius exponents in (11) are
\[
 \begin{array}{c|ccccc}
 \text{weight }v&b&c&u&p&q\\
 \text{exponent }e&b&c&\delta+s&\delta+b&\delta+c .
 \end{array}
 \tag{12}
\]
All weights are less than \(\delta<s\). Angle concavity gives
the strict lower bound
\[
 \frac1\delta\left[\sum_{(v,e)\ {\rm in}\ (12)}vf(e)
                                    -\delta f(\delta)-s f(s)\right].
 \tag{13}
\]
Here \(F_{r^e}(v)>(v/\delta)F_{r^e}(\delta)\), while
\(F_{r^s}(s)<(s/\delta)F_{r^s}(\delta)\).
Every exponent in (12) lies outside \([\delta,s]\):
\(b,c<\delta\), and
\(\delta+b>s,\delta+c>s,\delta+s>s\).
Moreover
\[
 \begin{split}
 \sum v&=\delta+s,\\
 \sum ve
 &=b^2+c^2+u(\delta+s)+p(\delta+b)+q(\delta+c)
   =\delta^2+s^2.
 \end{split}
 \tag{14}
\]
For the last identity, substitute \(u=s-\delta\),
\(p=\delta-b\), \(q=\delta-c\); the three last summands
are \(s^2-\delta^2,\delta^2-b^2,\delta^2-c^2\).
The secant line of the convex function \(f\) through
\(\delta,s\) lies below \(f\) outside that interval.
Summing with (14) makes the bracket in (13) nonnegative.
Strictness in the angle comparison proves positive height,
also when \(r=1\) makes \(f\) constant.
Continuity gives the stated compact uniformity.

The complete prism and crossing source theorems now apply,
with their original phases, prefactors and full Casimir normals.
Their local geometric packets are nonzero at all sufficiently
large levels, uniformly on these folded paths for
\(r\in[r_0,1]\). No uniform estimate at the origin is asserted.
The inverse crossing still uses its recorded reciprocal/conjugate
chart, rather than the same disk chart.

## 2. A uniformly controlled complete sampling frame

Fix \(N\ge2\), \(d=N-1\), and use the original centered
orthonormal basis \(f_a\), for which
\(\phi(f_af_b)=\delta_{ab}\). Put
\[
 \xi_j=\frac{j+1/2}{N},\quad w_j=w(\xi_j),\quad
 t_j(h)=-e^{-h w_j-2\pi i\xi_j},\quad
 E_j=\frac1{\sqrt N}\sum_{a=0}^d f_at_j(h)^a,\quad
 B_{aj}=\frac{t_j(h)^a}{\sqrt N}.
 \tag{15}
\]
The columns of \(B\) are the complete packets \(E_j\), not
evaluations only at distinct Casimir roots. Let \(P\) reverse
the sampling index, \(P_{ij}=\mathbf1_{i+j=d}\).
At \(h=0\), \(V=B(0)\) obeys
\[
                         V^*V=I,\qquad V^{\mathsf T}V=P.
 \tag{16}
\]
It is the original Newton frame with its known unit phases.

For \(A=\operatorname{diag}(0,\ldots,d)\) and
\(X=\operatorname{diag}(w_0,\ldots,w_d)\), the exact series
\[
 B(h)=\sum_{k\ge0}\frac{(-h)^k}{k!}A^kVX^k,\qquad
              \|B(h)-V\|\le e^{hd/2}-1
 \tag{17}
\]
uses \(\|X\|\le1/2\). Fix \(0<c<2\log2\) and
\(0\le h_N\le c/N\). Every singular value of \(B(h_N)\)
lies between
\[
                         m=2-e^{c/2}>0,\qquad M=e^{c/2}.
 \tag{18}
\]
This controls the full Gram, including its off-diagonal entries.
Set
\[
                     H=B^*B>0,\qquad S=B^{\mathsf T}B .
 \tag{19}
\]
Then \(m^2I\le H\le M^2I\). If \(Nh_N\to0\), \(B-V\to0\)
and \(H\to I\) in operator norm.

## 3. Exact orthogonality for both original pairings

Complementary nodes have equal folded weight, so
\[
                       \overline{t_j}=t_{d-j},\qquad
                       \bar B=BP.
 \tag{20}
\]
It follows that \(H=PS\), hence
\[
                  S=PH,\qquad \bar H=PHP.
 \tag{21}
\]
The second identity follows either from (20), or by transposing
the symmetric matrix \(S=PH\) and using \(H^*=H\).

Let the positive Hermitian inverse square root define
\[
                  U=BH^{-1/2},\qquad
                  \widehat E_j=\sum_aU_{aj}f_a .
 \tag{22}
\]
The symmetry in (21) implies
\(\overline{H^{-1/2}}=PH^{-1/2}P\): conjugating its positive
spectral decomposition gives the unique positive inverse square
root of \(\bar H\). Thus
\[
 \boxed{\qquad
 U^*U=I,\quad \bar U=UP,\quad U^{\mathsf T}U=P .
 \qquad}
 \tag{23}
\]
In particular
\[
 \langle\widehat E_i,\widehat E_j\rangle=\delta_{ij},
       \qquad \phi(\widehat E_i\widehat E_j)=P_{ij}.
 \tag{24}
\]
For a direct check of the last identity,
\[
 U^{\mathsf T}U=
 \overline{H^{-1/2}}\,S H^{-1/2}
 =PH^{-1/2}P\,PHH^{-1/2}=P .
\]
No positive form has been substituted for the original bilinear
form. Both pairings in (24) are exact on all \(N\) channels.

## 4. What is transported, and what still needs an estimate

The original scalar source is unchanged if every tensor is
transported through the unitary \(U\). If \(M_f\) is multiplication,
\(\mathsf J_f\) the genuine physical turn, and \(\ell_f\) an
original prescribed closing, their coordinate formulas are
\[
 \begin{split}
 M_U&=U^*M_f(U\otimes U),\qquad
 \mathsf J_U=U^*\mathsf J_fU,\\
 R_U^+&=\sqrt N\,U^*\delta_0,\qquad
 R_U^-=\sqrt N\,U^*\delta_d,\qquad
 \ell_U=\ell_fU .
 \end{split}
 \tag{25}
\]
All adjacent changes cancel in the expression. Positive vector
norms, operator Hilbert--Schmidt norms and the previously recorded
compiler budgets are unchanged. In covariant form the dual basis
is \(\widehat E^j=\widehat E_{d-j}\), so sewing uses \(P\)
exactly.

The sampling reflection \(P\) in (23)--(24) must not be confused
with a claim about the matrix of the physical turn. That matrix
is the transported operator in (25), including its actual phases.

The two signed crossing operators also retain a useful exact relation.
In centered coordinates write their matrices as \(A_f^\pm\).
The centered tensor is symmetric and obeys
\(\overline{C_{abc}}=C_{d-a,d-b,d-c}\). Hence
\[
 A_f^-=\mathsf J_f(A_f^+)^*\mathsf J_f,\qquad
 A_U^-=\mathsf J_U(A_U^+)^*\mathsf J_U .
 \tag{25a}
\]
Here \(\mathsf J_f\) is the centered reversal, and
\(\mathsf J_U\) is its full transported unitary selfadjoint
operator. This is an operator identity with every channel retained.
It makes neither crossing unitary, nor supplies a same-disk
pointwise estimate for the inverse kernel.

The raw tensor
\[
 T^E_{ijk}=\phi(E_iE_jE_k)
        =N^{-3/2}\mathcal C_N(t_i,t_j,t_k)
 \tag{26}
\]
has the source-calibrated geometric asymptotic at strict prism
nodes by Theorem 1 and the full transport theorem. The raw
positive-crossing block likewise equals
\(N^{-1}\mathcal K_N^+(t_i,t_j)\) on strict tetrahedron nodes.
These estimates include the thin layers \(h_N\le c/N\).

Polar orthogonalization is still a full matrix operation. Writing
\(L=H^{-1/2}\), its covariant tensor is
\[
                 T^{\widehat E}_{ijk}
                 =\sum_{\alpha,\beta,\gamma}
                    L_{\alpha i}L_{\beta j}L_{\gamma k}
                                      T^E_{\alpha\beta\gamma}.
 \tag{27}
\]
Although \(\|L\|\le m^{-1}\), this bound alone does not
preserve the leading asymptotic of any particular entry or
closing. The mixing and its off-region contributions remain
part of the source. No angular spiral has been substituted
for an original closed coefficient contour.

We have an explicit complete orthogonal basis adapted to a
reflection-symmetric growing sample family. Proving packet
localization through its full polar matrix, compatibility of
geometric attachments and nonzero final closing still requires
additional estimates. No new knot-volume or finite-exception
theorem is asserted.

## Complete proof sources

All complete matching texts were read:

| Source | SHA-256 |
|---|---|
| [Angle-weighted path and convexity method](research_angle_weighted_geometric_source_path.md) | 5f95115b02515db314183b7e581ddc11c6852191d7764547545103986f628f2d |
| [Full spiral sampling and source transport](research_spiral_boundary_sampling_gram.md) | 301eb215a1da04579c65d2638bb8b69ba700cc6d57cc39a0655f930131b2d6df |
| [Original centered compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Independent-modulus prism source](research_centered_tensor_full_prism_source_transport.md) | eb43e287eca5933b70de3b6362a81f92d46bb2e121f0eb5716793c107adaef10 |
| [Independent-modulus crossing source](research_centered_signed_crossing_endpoint_source.md) | 40adef586a0c2c5c418caf5c8ea120391cf0ba308a7f7b2ad6649be044a77154 |

The new points are the folded growing law and its exact compatibility
with polar orthogonalization of both original pairings. No novelty
is claimed for matrix polar decomposition or elementary convexity.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
