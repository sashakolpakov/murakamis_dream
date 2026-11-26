# Exact removal of a physical crossing from the Gauss factor

Private written proof, 18 November 2026.

On every upper-chamber two-head degree block, the actual finite Gauss
factor times the physical checked crossing is a scalar times
\(E^H F^H\), where \(H\) is the complementary degree. The equality
includes every Casimir Jordan derivative. It replaces a specific
anti-triangular crossing interface by a polynomial of degree \(H\);
it does not replace that polynomial by its classical symbol.

This is a fixed-root, complete-meridian identity. Its insertion into
a meridian-dependent source keeps an explicit normal defect. No
large-power coherent estimate or geometric-cycle contribution is
claimed.

## 1. Actual operators and the statement

Use the complete directs G, H, L, and F pinned below. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad f_a=(Q;Q)_a.
 \tag{1}
\]
All operators until Section 5 are at \(M=1\). On two actual heads,
\[
 F=F_1+K_1^{-1}F_2,\qquad E=E_1K_2+E_2,\qquad
 \Omega=FE+qK+q^{-1}K^{-1}.
 \tag{2}
\]
Consider their physical integer-degree block
\[
 \mathcal V_T=\operatorname{span}\{|a,T-a\rangle:0\le a\le T\},
 \qquad \lceil d/2\rceil\le T\le d.
\]
Set
\[
 H=d-T,\qquad L=d-2H=T-H,\qquad
 C=K|_{\mathcal V_T}=Q^{-T-1}=Q^H.
 \tag{3}
\]
Thus \(0\le H\le T\) and \(2H<N\). The letter \(H\) here is
an integer, not a lowering factorial or a source normalization.

Let \(A_T\) be G's actual \(A_N=q_FE_\Sigma^d i_d\) restricted
to these two remaining heads and this block. G's exact finite formula is
\[
 A_N=
 \sum_{n=0}^d\frac{Q^{-n}x^{-n}}{f_n}
       \frac{H_d(1)}{H_n(1)}F^nE^nK^{d-n},
 \qquad
 H_n(1)=Q^{-n(n+1)/2}f_n,\quad H_d(1)=(-1)^dN.
 \tag{4}
\]
Let \(R_T\) be the original positive physical checked crossing on
these two heads, including its scalar \(\kappa\). It is the
physical tail crossing, not the triangular reduced generator
\(\kappa S_2D\). Write \(R_T=\kappa r_T(\Omega)\) as in H.

Define
\[
 P_H(z)=\prod_{\ell=0}^{H-1}(z-\lambda_\ell),\qquad
 \lambda_j=q^{2j+1}+q^{-2j-1},\qquad P_0=1.
 \tag{5}
\]
Then the exact operator identity is
\[
 \boxed{\quad
 A_TR_T=R_TA_T=\kappa c_H P_H(\Omega)
                    =\kappa c_H E^HF^H\big|_{\mathcal V_T},
 \qquad
 c_H=\frac{(-1)^{d-H}Nq^{3H^2}}{f_{2H}}.
 \quad}\tag{6}
\]
Every denominator is a nonzero literal root factorial. At \(H=0\),
\[
                         A_dR_d=(-1)^dN\kappa I.
 \tag{7}
\]
The proof below checks values and the actual first Casimir derivatives,
rather than identifying polynomials only on distinct spectral points.

The reversed ordered-product identity follows from (2):
\[
 E^HF^H
 =\prod_{s=1}^H
       (\Omega-qQ^{-s}K-q^{-1}Q^sK^{-1}).
 \tag{8}
\]
On (3), the \(s\)-th root is \(\lambda_{H-s}\). This proves the
second equality in (6) without changing the order of \(E\) and \(F\).
Both \(A_T\) and \(R_T\) commute with \(\Omega\) and with each other.

## 2. The actual spectral data, including the crossing derivative

H proves that the characteristic polynomial of the complex-symmetric
Jacobi block \(\Omega|_{\mathcal V_T}\) is
\[
             \prod_{j=0}^T(z-\lambda_j).
 \tag{9}
\]
Its normalized continuant column \(v(z)\) has first component one.
Every distinct node is either simple or has a size-two chain
\(v(\lambda),v'(\lambda)\). A collision is exactly
\[
                         j+\ell=d.
\]
The unpaired simple nodes are \(j<H\). All other non-self nodes
are paired within \(H,\ldots,T\). If \(N\) is odd, the self node
\(j=d/2\) is simple. These columns and chains form the entire block.

The actual crossing values are
\[
                  r_T(\lambda_j)=\nu_j=(-1)^jq^{j(j+1)}.
 \tag{10}
\]
For a double node put
\(\Delta_j=q^{2j+1}-q^{-2j-1}\ne0\). Its actual derivative is
\[
             \boxed{\quad
       \frac{r_T'(\lambda_j)}{\nu_j}
                     =\frac{2j-d}{2\Delta_j}.
             \quad}\tag{11}
\]
Here a prime means derivative of the crossing's polynomial in the
Casimir, not a meridian derivative.

For completeness, (11) can be obtained from H's actual ordinary
highest-weight lift before confluence. Vary the quantum parameter to
\(\zeta\) near \(q\), with highest weight \(d=N-1\),
\(Q_\zeta=\zeta^2\), and \(x_\zeta=\zeta^d\). H's highest vector
at degree \(j\), with first component one, has last component
\[
        (-1)^j x_\zeta^{-j}Q_\zeta^{j(j-1)/2}.
\]
The first row of the original checked crossing on degree \(j\)
has only its last column, with coefficient
\(\kappa(\zeta)x_\zeta^{-j}\). This is also immediate from the
literal flip--Cartan--Euler matrix: an output first occupation zero
allows only zero transfer and input \(|j,0\rangle\).
Consequently the stripped crossing eigenvalue is
\[
 \nu_j(\zeta)=(-1)^j\zeta^{j(j-2d-1)}.
 \tag{12}
\]
Its actual Casimir eigenvalue is
\(\lambda_j(\zeta)=\zeta^{2d+1-2j}
                       +\zeta^{-2d-1+2j}\).

For \(\ell=d-j\), the two normalized actual columns coalesce to
H's derivative column. Therefore
\[
 r_T'(\lambda_j)
  =\lim_{\zeta\to q}
       \frac{\nu_j(\zeta)-\nu_\ell(\zeta)}
            {\lambda_j(\zeta)-\lambda_\ell(\zeta)}.
\]
The logarithmic derivatives of numerator and denominator at \(q\)
are respectively \(N(\ell-j)\nu_j\) and \(-2N\Delta_j\).
This proves (11). The common \(\zeta\)-derivative of the crossing
matrix cancels in this divided difference. Thus no arbitrary
off-grid interpolation of the values (10) has been used.

## 3. Values and marked factorial derivatives of the Gauss factor

L gives the exact factorial representative of G's finite polynomial
on each physical marked primary germ, including its nilpotent part.
Write \(F_N\) for F's marked factorial:
\[
 F_N(n)=f_n,\qquad
 F_N(z+1)=(1-Q^{z+1})F_N(z),\qquad
 F_N(z)F_N(d-z)=N e^{i\pi z(z-d)/N}.
 \tag{13}
\]
The last identity is F's exact reflection, with its phase retained.

At \(\lambda_j\), the two factorial labels in L are the residues
of \(T-j\) and \(T+j+1\) in \(0,\ldots,d\). If \(j<H\), their
sum is \(2T+1\ge N\). L then says that the entire root primary
restriction of \(A_T\) is zero. In this block that node is simple.
Also \(P_H(\lambda_j)=0\), so (6) holds there.

For \(H\le j\le T\), the marked labels are
\[
                         T-j,\quad j-H,
\]
with sum \(L<N\). Hence
\[
 A_T(\lambda_j)
       =(-1)^dNC^d\,\frac{f_L}{f_{T-j}f_{j-H}}.
 \tag{14}
\]
All these values are nonzero. Direct factorization of the node
differences gives
\[
 P_H(\lambda_j)
     =q^{-H(2j+1)}\,\frac{f_{j+H}}{f_{j-H}}.
 \tag{15}
\]
For example,
\(\lambda_j-\lambda_\ell
 =q^{-2j-1}(1-Q^{j-\ell})(1-Q^{j+\ell+1})\);
the two consecutive intervals telescope to (15).
Root reflection in (13) gives
\[
 f_{T-j}f_{j+H}
       =N(-1)^{j+H}Q^{(j+H)(j+H+1)/2}.
\]
Combining (10),(14),(15) therefore yields
\[
 \frac{A_T(\lambda_j)\nu_j}{P_H(\lambda_j)}
           =(-1)^T C^d q^{-H^2}f_L.
 \tag{16}
\]
Since \(f_Lf_{2H}=NQ^{H(2H+1)}\), \(C^d=Q^{Hd}\), and
\(q^{2HN}=1\), the right side is exactly \(c_H\) in (6).

Values alone do not suffice on a double node. Choose a local
logarithmic coordinate \(j=j(z)\) near either label of such a
node by
\[
       z=q^{2j+1},\qquad \Omega=z+z^{-1},\qquad
       \frac{dj}{d\Omega}=\frac{N}{2\pi i\,\Delta_j}
                         \quad\hbox{at the node}.
 \tag{17}
\]
L's marked functional calculus implies that a representative of
the value and first Casimir jet of \(A_T\) is
\[
 \frac{(-1)^dNC^df_L}{F_N(T-j)F_N(j-H)}.
 \tag{18}
\]
This asserts equality on the actual primary block, not equality
of that factorial function with the finite polynomial at arbitrary
scalar arguments.

As an ordinary local analytic identity, (8) and the finite shifts
in (13) give
\[
 P_H(z+z^{-1})=z^{-H}
                  \frac{F_N(j+H)}{F_N(j-H)}.
 \tag{19}
\]
Dividing (18) by (19), and applying exact reflection with
\(v=j+H\), gives the jet representative
\[
 \frac{A_T}{P_H}
   =(-1)^d C^d f_L\,z^H
                    \exp[-i\pi(j+H)(j+H-d)/N].
 \tag{20}
\]
The notation in (20) means the marked representative for the
left side on that primary germ. Its logarithmic \(j\)-derivative
is \(i\pi(d-2j)/N\). By (17),
\[
 \left(\frac{A_T'}{A_T}
            -\frac{P_H'}{P_H}\right)(\lambda_j)
                  =\frac{d-2j}{2\Delta_j}.
 \tag{21}
\]
This cancels (11), so
\[
 (A_T r_T)'(\lambda_j)=c_HP_H'(\lambda_j).
 \tag{22}
\]
There is no derivative test at the self node, which is simple;
its value was already covered by (16). Equations (14)--(22),
the simple zero nodes, and H's complete chain basis prove (6)
on the full physical block, including every nilpotent entry.

## 4. What the factorization changes in the actual kernel

The block \(\Omega\) is tridiagonal in \(|a,T-a\rangle\).
Thus \(P_H(\Omega)\) has bandwidth at most \(H\):
\[
          (A_TR_T)_{ba}=0\qquad\text{if }|b-a|>H.
 \tag{23}
\]
This is an exact finite support reduction, not a decay estimate.

For any ordered actual outer matrices or source rows \(L_0,B_0\),
\[
 L_0A_TR_TB_0=\kappa c_H L_0E^HF^HB_0.
 \tag{24}
\]
One may use the equality also in a finite coherent convolution,
because that convolution is the exact resolution of the same
matrix product. All original binomial factors, finite identity
caps, and external source scalars remain on their respective legs.
No inverse Casimir measure or diagonalizability assumption is
needed to insert (24).

The complementary highest-row relation is likewise exact.
The first physical row of \(R_T\) is
\(\kappa x^{-T}\langle T|\), so commutation gives
\[
              \langle T|A_T
                  =\kappa^{-1}x^T\langle0|A_TR_T.
 \tag{25}
\]
This is a relation for the physical checked crossing. It does not
identify it with the triangular reduced \(R_1\) generator.

There is a source-exact coefficient contour for the remaining power.
Define the actual finite Euler polynomials
\[
                    E_N(tX)=\sum_{n=0}^d t^nX^n/f_n .
\]
Then, with every finite cap retained,
\[
 E^HF^H=f_H^2[\lambda^H\mu^H]\,
                         E_N(\lambda E)E_N(\mu F).
 \tag{26}
\]
The coefficient means two small positively oriented circles about
zero, with factors \(d\lambda/\lambda^{H+1}\) and
\(d\mu/\mu^{H+1}\). Equation (26) is exact for all \(H\) in (3).
It does not estimate that extensive coefficient from a small-activity
asymptotic, nor select a later deformed contour.

## 5. Routed opposite source and the normal terms still required

G's actual two-tail routing is
\[
 T_{\rm op}
  =\mathcal B_3(W_\tau^{-1})A_ND_{\rm top}\mathscr C_2,
 \qquad J_{\rm op}=D_N(MK)^{-1}T_{\rm op}.
 \tag{27}
\]
The factor \(D_{\rm top}\), the balanced turnover, the routed word,
and the source normalization keep exactly G's order. At the root,
on the degree block (3), (6) permits the substitution
\[
 A_T=\kappa c_HE^HF^HR_T^{-1}
 \tag{28}
\]
inside (27). A physical positive crossing immediately next to \(A_T\)
is thereby absorbed by (24). No unrelated crossing is commuted
through an exterior to create such an adjacency.

In particular (6) must not be differentiated as though it were a
proved meridian-family identity. To state the retained normal
precisely, keep the original analytic fixed-root matrices and define
\[
 \mathcal D_T(M)=
 A_T(M)R_T(M)-\kappa(M)c_HE(M)^HF(M)^H.
 \tag{29}
\]
The number \(c_H\) in this definition is the fixed-root scalar (6).
The preceding proof says \(\mathcal D_T(1)=0\); it supplies no
formula or bound for its first normal. The exact family rewrite is
\[
 A_T(M)=
 \{\kappa(M)c_HE(M)^HF(M)^H+\mathcal D_T(M)\}R_T(M)^{-1}.
 \tag{30}
\]
Hence \(\mathcal D_T(M)\) remains inside (27) and inside any
meridian finite part used by the original sewn source. Its root
zero alone does not remove it beside a meridian pole.
Similarly, (6) is not a quantum-parameter normal identity.

The result pays the literal physical-crossing interface, its
complete Jordan data, and a shorter exact coefficient contour.
It does not yet pay an estimate for \(E^HF^H\) at \(H\) proportional
to \(N\), an entire signed word on a common coherent chart, or a
nonzero geometric contribution to the original closing cycle.

## Complete proof directs

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  SHA256 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* H: notes/actual_complete_casimir_hermite_packet.md,
  SHA256 a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.
* L: notes/research_marked_gauss_functional_calculus.md,
  SHA256 7f8c7c0be05331e7c0679c5a26374bbcb4b38b817c36a1f4ac4e16d4c1739095.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.

All four complete directs were freshly read nontruncated in this
author sequence. Every used implication was checked. Only written
mathematics and text/hash operations were used; frozen and public
files were not changed.

