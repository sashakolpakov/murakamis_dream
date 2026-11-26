# A physical Fourier band and a squared complementary Gauss operator

Private written proof, 19 November 2026.

The complementary two-head Gauss factor has an exact Fourier-band
range. This is a statement about its original physical coordinates,
not about the conditioning of a Casimir eigenbasis. An explicit family
of band-limited packets has exponentially small mass outside the
physical occupation window. On a growing packet subspace, restriction
to that window is consequently an exponentially accurate isometry.

There is also an exact fused-square identity: multiplying the
complementary factor by the physical crossing and squaring gives a
specified scalar times a single ordered power of the actual lowering
and raising totals. Both assertions concern universal two-head
building blocks, rather than a particular knot. They do not prove that
the closing source preserves these packets or has a nonzero pairing
with them. The complete proof directs are G, L, H and J, pinned below.

## 1. The actual complementary polynomial

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\qquad f_a=(Q;Q)_a.
\]
Use the actual two-head totals of G and H, with
\[
 \Omega=FE+qK+q^{-1}K^{-1}.
\]
Fix an integer \(H\) with \(1\le H<N/2\), and set
\[
 T=d-H,\qquad C=Q^H,\qquad n=N-2H.
 \tag{1}
\]
The low physical space is
\(V_T=\operatorname{span}\{|a,T-a\rangle:0\le a\le T\}\).
Its total Cartan is \(K=C\).

G's Gauss polynomial, with its Laurent Cartan argument displayed, is
\[
 A_N(k,z)=H_d\sum_{j=0}^{d}
 \frac{Q^{-j}x^{-j}}{f_j H_j}
 \left\{\prod_{b=0}^{j-1}(z-qQ^bk-q^{-1}Q^{-b}k^{-1})\right\}
 k^{d-j},
 \quad H_j=Q^{-j(j+1)/2}f_j,
 \quad H_d=(-1)^dN.
 \tag{2}
\]
The letter \(H_d\) in (2) denotes the lowering product; the integer
\(H\) in (1) is unrelated. Define the complementary matrix by
\[
                 A^\vee=A_N(C^{-1},\Omega|_{V_T}).
 \tag{3}
\]
This is a literal finite polynomial in the actual Jacobi matrix.
It also has the ordered form
\[
 A^\vee=H_d\sum_{j=0}^{d}
      \frac{Q^{-j}x^{-j}}{f_jH_j}
                    E^jF^jK^{-d+j}\big|_{V_T}.
 \tag{4}
\]
Indeed the reversed ordered product is
\[
 E^jF^j=\prod_{b=1}^{j}
       (\Omega-qQ^{-b}K-q^{-1}Q^bK^{-1});
\]
putting \(b=b'+1\) turns these roots into the roots of (2) with
\(k=K^{-1}\). Formula (4) retains the full transfer cap \(j\le d\).

For clarity this polynomial is the actual complementary-degree
operator in the root routing. Let \(\mathsf W_2\) complement the two
occupations and reverse their order, without a sign, and put
\(\mathsf L=\mathsf W_2q^{\mathsf n}\), where \(\mathsf n\) is total
occupation. The exact degree/turnover factor of G is \(\kappa^2\mathsf L\).
It maps degree \(T\) to degree \(2d-T\). Direct application to a
one-head basis vector gives, with the reversal included for totals,
\[
 \mathsf L^{-1}E\mathsf L=-q^{-1}F,\qquad
 \mathsf L^{-1}F\mathsf L=-qE,\qquad
 \mathsf L^{-1}K\mathsf L=K^{-1},\qquad
 \mathsf L^{-1}\Omega\mathsf L=\Omega.
 \tag{5}
\]
For example on one head the first identity has coefficient
\(q^{-1}(Q^{a+1}-1)\); its endpoint is zero as well.
The last identity follows from
\(EF-FE=(q-q^{-1})(K-K^{-1})\).
Conjugating G's full root Gauss sum by (5) proves
\[
 \mathsf L^{-1}A_N|_{V_{2d-T}}\mathsf L=A^\vee.
 \tag{6}
\]
Thus no integer degree has been replaced by its residue modulo \(N\).

## 2. Which primary components survive

H gives the complete Jacobi spectrum on \(V_T\):
\[
 \lambda_j=qQ^j+q^{-1}Q^{-j},\qquad 0\le j\le T,
 \quad \det(z-\Omega)=\prod_{j=0}^{T}(z-\lambda_j).
 \tag{7}
\]
The nodes \(j<H\) are simple. The remaining interval
\(H\le j\le T=N-H-1\) contains both labels of each double node,
and the possible simple self node. H supplies the whole size-two
Jordan blocks; there are no larger blocks.

For the Cartan argument \(C^{-1}\) the physical factorial labels
at a simple node \(j<H\) are
\[
                         H-j-1,\qquad H+j.
\]
Their sum is \(2H-1<N\), so L's marked factorial identity gives
\[
 A^\vee|_{\lambda_j}=
        H_d C\frac{f_{2H-1}}{f_{H-j-1}f_{H+j}}\ne0.
 \tag{8}
\]
For a remaining node take its lower label
\(H\le j\le d/2\). The labels are instead
\(N+H-j-1,H+j\), whose sum is \(N+2H-1\).
L's upper-primary identity says that the entire restriction of
\(A^\vee\) to that generalized eigenspace is zero.

Here applying L does not identify a new meridian family with the old
one. Its local divisibility identity is an identity of holomorphic
functions modulo
\(C_N(z)+k^N+k^{-N}\). This relation holds at \(k=C^{-1}\) on our
actual matrix because it holds at \(k=C\), and is symmetric in
\(k,k^{-1}\). The factorial numerator depends on the sum of the two
marked logarithms. That sum is constant on a fixed-Cartan primary
block, including its nilpotent parts. Its upper zero therefore
annihilates the entire block, not just its eigenvalue. This also
covers the self node without dividing by the spectral discriminant.

Consequently \(A^\vee\) has rank exactly \(H\). Its image is the
sum of the unpaired simple eigenspaces. Its restriction to that image
is invertible at each fixed level. No uniform inverse norm follows.

## 3. The image is a literal restricted Fourier band

Define physical vectors
\[
          u_s(a)=x^aQ^{-sa},\qquad 0\le a\le T,
                          \quad 0\le s<H.
 \tag{9}
\]
They are linearly independent: their first \(H\) rows form a
Vandermonde matrix at distinct points \(Q^{-s}\).

We verify invariance without diagonalizing \(\Omega\). H's Jacobi
entries, in the present notation, are
\[
 \alpha_a=(CQ^{a+1}-1)(1-Q^{a+1}),\qquad
 \beta_a=2q(1+C)Q^a-qC(1+Q)Q^{2a}.
 \tag{10}
\]
Use zero missing arrows. Substituting (9) into (10) gives exactly
\[
 \begin{split}
 \Omega u_s={}&\lambda_su_s
   +q(1+C)(2-Q^s-Q^{-s})u_{s-1}\\
   &+Cq(Q^s+Q^{1-s}-1-Q)u_{s-2}.
 \end{split}                                                   \tag{11}
\]
The first lower coefficient vanishes at \(s=0\); the second
vanishes at \(s=0,1\). Thus negative-index vectors are absent.
To check (11), put \(y=Q^a\) and divide its interior row by
\(x^aQ^{-sa}\). The constant, linear and quadratic coefficients
in \(y\) are precisely the three displayed coefficients.
The same formula holds at both endpoints because
\(\alpha_{-1}=\alpha_T=0\).

The span of (9) is invariant and has the distinct diagonal values
\(\lambda_0,\ldots,\lambda_{H-1}\). By (7) these values are all
simple in the entire space. Its dimension is \(H\), so (8),(11)
prove the exact equality
\[
 \boxed{\quad
 \operatorname{im}A^\vee
      =\operatorname{span}\{x^aQ^{-sa}:0\le s<H\}_{a=0}^{T}.
 \quad}                                                        \tag{12}
\]

On the full cyclic set \(a=0,\ldots,N-1\), the characters
\(N^{-1/2}Q^{-sa}\) form the unitary discrete Fourier basis.
Equation (12) is its frequency band \(0\le s<H\), restricted to
the physical window \(0\le a\le T=N-H-1\), followed by the unitary
diagonal \(x^a\). This is an exact Fourier statement.
It does not say that restriction is uniformly conditioned on the
whole band, or that its orthogonal projector is the bilinear Casimir
projector. Those are different operators.

## 4. Packets on which physical restriction is almost isometric

Assume now that \(H/N\) stays in a compact subinterval of \((0,1/2)\).
Fix a small \(\delta>0\) and \(\epsilon>0\), and choose
\(L=\lfloor\delta N\rfloor\) and \(s_0\) so that
\([s_0,s_0+L]\subset[0,H-1]\). Leave a fixed proportional margin
if desired. Let \(a_0\) be an integer a fixed proportional distance
from both endpoints of \([0,T]\). Set
\[
 b^{a_0}_{s_0+j}=
       \frac{2^{-L}\binom Lj Q^{a_0(s_0+j)}}{\nu_L},
 \quad 0\le j\le L,\qquad
 \nu_L^2=4^{-L}\binom{2L}{L},
 \tag{13}
\]
and set its other frequency coefficients to zero.
Its Euclidean norm is one. The full inverse Fourier transform,
with the diagonal in (12), has exact modulus
\[
 |v^{a_0}_a|=
    \frac{|\cos(\pi(a-a_0)/N)|^L}{\sqrt N\,\nu_L}.
 \tag{14}
\]
The bounds \(cL^{-1/2}\le\nu_L^2\le CL^{-1/2}\) follow, for
example, by integrating \(|\cos(t/2)|^{2L}\): its central arc has
width comparable to \(L^{-1/2}\), and its complement has a Gaussian
upper bound. Therefore
\[
 |v^{a_0}_a|\le C N^{-1/4}
       \exp[-c\operatorname{dist}_N(a,a_0)^2/N].
 \tag{15}
\]
In particular the squared norm omitted by physical restriction is
\(O(e^{-cN})\), uniformly for the indicated centers.

We also need an estimate on entire packet spans. Full Plancherel
gives, with \(\theta=2\pi(a_0-a_1)/N\),
\[
 |\langle v^{a_0},v^{a_1}\rangle|
 =\frac{\left|\sum_{j=0}^{L}\binom Lj^2e^{ij\theta}\right|}
             {\binom{2L}{L}}
 \le C\exp[-c\operatorname{dist}_N(a_0,a_1)^2/N].
 \tag{16}
\]
Here is a bound without a growing prefactor. The numerator is the
modulus of \([z^L](1+z)^L(1+e^{i\theta}z)^L\). Cauchy's integral
on \(|z|=1\) bounds it by
\[
 \frac C{\sqrt L}
          [2(1+|\cos(\theta/2)|)]^L.
\]
Indeed the product of the two factor moduli is
\(2|\cos(\theta/2)+\cos(t+\theta/2)|\); relative to its maximum
its integral is bounded by two Gaussian arcs, uniformly in
\(\theta\). Divide by
\(\binom{2L}{L}\ge c4^L/\sqrt L\) and use
\((1+|\cos(\theta/2)|)/2\le e^{-c\operatorname{dist}(\theta,2\pi\mathbb Z)^2}\).
This proves (16).

Choose centers in the interior physical window separated by
\(K\sqrt N\), where \(K\) is a sufficiently large fixed number.
There are at least \(c\sqrt N\) such centers. Circular separation
and (16) bound every off-diagonal row sum of their Gram matrix by
\(2C\sum_{j\ge1}e^{-cK^2j^2}<1/2\).
The elementary inequality \(2|z_i z_j|\le|z_i|^2+|z_j|^2\)
then puts all its quadratic forms between
\(\tfrac12\sum|z_i|^2\) and \(\tfrac32\sum|z_i|^2\).

The omitted-window Gram has each entry \(O(e^{-cN})\), by (15)
and Cauchy--Schwarz. Its operator norm is at most the number of
centers times that bound, hence \(O(e^{-c'N})\).
If \(\mathcal P_N\) denotes the full cyclic packet span and
\(\mathsf R_T\) denotes physical restriction, this proves
\[
 \boxed{\quad
 \dim\mathcal P_N\ge c\sqrt N,\qquad
 (1-Ce^{-c'N})\|v\|_2^2
       \le\|\mathsf R_Tv\|_2^2\le\|v\|_2^2
            \quad(v\in\mathcal P_N).
 \quad}                                                        \tag{17}
\]
Its restricted packets belong exactly to (12). No spectral inverse
or choice of an eigenvector norm enters this construction.

## 5. Squaring after a physical crossing gives one ordered power

Let \(R_T\) be the actual positive checked crossing on \(V_T\),
including its original scalar \(\kappa\). H gives its simple-node
values \(\kappa\nu_j\), with
\(\nu_j=(-1)^jq^{j(j+1)}\), and its actual Jordan derivatives.
It commutes with \(\Omega\) and hence with (3).
Then
\[
 \boxed{\quad
       (A^\vee R_T)^2
       =-\kappa^2 Q^{2H-H^2}f_{2H-1}^{\,2}
                     F^{N-2H}E^{N-2H}\big|_{V_T}.
 \quad}                                                        \tag{18}
\]
Every power and scalar in this formula is literal.

To prove it, the normal ordering in G gives
\[
 F^nE^n=\prod_{l=H}^{N-H-1}(\Omega-\lambda_l),\qquad n=N-2H.
 \tag{19}
\]
On a simple \(j<H\), factor the node differences as
\(\lambda_j-\lambda_l=qQ^j(1-Q^{l-j})(1-Q^{-j-l-1})\).
The two product intervals coincide modulo \(N\), so
\[
 (F^nE^n)_j=q^nQ^{nj}
       \left(\frac{f_{N-H-j-1}}{f_{H-j-1}}\right)^2.
 \tag{20}
\]
The elementary root complement is
\[
 f_{d-b}=N(-1)^bQ^{b(b+1)/2}/f_b.
\]
It follows by multiplying the missing factors in \(f_d=N\).
Use it in (20), and use \(Q^{Nj}=1\), to obtain
\[
 (F^nE^n)_j=
   \frac{q^nN^2 Q^{H(H+1)+j(j+1)}}
        {f_{H-j-1}^{\,2}f_{H+j}^{\,2}}.
 \tag{21}
\]
On the other side (8) and \(\nu_j^2=Q^{j(j+1)}\) give the same
value times \(\kappa^2C^2f_{2H-1}^2q^{-n}Q^{-H(H+1)}\).
Since \(q^{-n}=-Q^H\), this scalar is exactly the one in (18).

On every other primary block \(A^\vee\) is the zero matrix.
The product (19) contains each double-node factor twice and the
possible self-node factor once, so it is also the zero matrix on
that whole complement. This checks the actual Jordan multiplicities;
no interpolation of distinct eigenvalues is substituted for a
matrix proof. Completeness in H proves (18) on the whole block.

The nonzero eigenvalues of (19) are positive real numbers: all
\(\lambda_j\), \(j<H\), exceed every \(\lambda_l\) in (19).
This spectral fact is not Hermitian positivity in the physical norm.
Likewise (18) is a square, not an adjoint square and not a formula
for the absolute square of a closed knot invariant.

## 6. Normal data and the remaining transport problem

All identities through (18) are fixed-root identities. If (18) is
inserted into a meridian-dependent source, keep the actual
\(\mathsf L(M)^{-1}A_N(M)\mathsf L(M)\), crossing and ordered
power before differentiating. Their difference from the displayed
root factorization has value zero at \(M=1\); its first derivative
has not been shown zero. No root factorization is differentiated
as a whole-meridian identity here.

The entire band in (12) is preserved by the complementary matrix
and its physical crossing. This does not make the much smaller
well-conditioned packet span in (17) invariant. No norm bound for
their transport on that packet span, no prescribed closing overlap,
and no comparison with a nonreal geometric period is supplied.
In particular a large operator norm or a nonzero squared kernel
does not imply a nonzero closed trace.

What is available is a concrete Fourier realization of the surviving
source components, an explicit positive physical norm on selected
packets, and the exact fused identity (18). A Plancherel argument
for the original source must additionally control transport and
the actual boundary functional in these coordinates.

## Complete proof directs

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  489 lines, SHA256
  42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* L: notes/research_marked_gauss_functional_calculus.md,
  487 lines, SHA256
  7f8c7c0be05331e7c0679c5a26374bbcb4b38b817c36a1f4ac4e16d4c1739095.
* H: notes/actual_complete_casimir_hermite_packet.md,
  321 lines, SHA256
  a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.
* J: notes/research_opposite_polarization_source_kernel.md,
  639 lines, SHA256
  d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

Only written mathematics and text operations are used. H was freshly
read in full during this author sequence; the complete matching G,
L and J reads from the immediately preceding active review sequence
are explicitly retained unchanged. Author readback, all matching pins
and independent complete-direct review are required before adoption.
