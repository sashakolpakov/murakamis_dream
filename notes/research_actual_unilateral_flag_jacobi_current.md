# An inverse-free routed flag mark and its actual block Jacobi current

Private written proof, 18 November 2026.

A literal unilateral lowering coupon gives an inverse-free version
of the balanced framing coordinate. It satisfies an exact first
flag row and a finite quantum-oscillator identity with its full top
wall. Removing the first meridian-prefix factor then expresses the
routed mark as an operator-valued tridiagonal matrix in the first
occupation. The other-head blocks and the original source remain.

The insertion is bounded on a parameter collar of quantum radius
\(O(N^{-1})\), with fixed ordinary quantum normals of polynomial
size \(O(N^k)\). Its exact difference from the previous bounded
mark is retained, including an order-one endpoint contribution.
Neither a full quantum eigenflag nor a scalar q-Hahn or Newton
spectral problem follows from these calculations.

The complete proof directs are C, B, and M, pinned below.

## 1. The literal unilateral coupon

For \(N\ge2\), on the actual \(N\)-dimensional factorial head define
\[
 S_-e_a=e_{a-1}\ (a>0),\qquad S_-e_0=0,\qquad
 Q_{\rm f}=-q^{-1}S_- .
 \tag{1}
\]
Keep the matrices, parameters, and zero arrows of C:
\[
 \begin{split}
 K e_a&=-M q^{-1}Q^{-a}e_a,\\
 \mathcal E e_a&=(MQ^{-a}-M^{-1})e_{a-1}\quad(a>0),
       &\mathcal E e_0&=0,\\
 F e_a&=(1-Q^{a+1})e_{a+1}\quad(a<N-1),
       &F e_{N-1}&=0,\qquad Q=q^2 .
 \end{split}
 \tag{2}
\]
The letter \(Q_{\rm f}\) denotes a matrix; \(Q\) is the scalar.
For every \(q,M\ne0\), one has the exact identity
\[
                  \boxed{\quad
           \mathcal E=(K+qM^{-1}I)Q_{\rm f}.
                  \quad}
 \tag{3}
\]
On input \(a>0\), the coefficient of the right side is
\[
 -q^{-1}\big(-Mq^{1-2a}+qM^{-1}\big)
                           =Mq^{-2a}-M^{-1}.
 \tag{4}
\]
On \(a=0\) both sides vanish. The output row \(a-1\), not
the input row, is used in (4). No inverse of \(K+qM^{-1}I\)
has been taken. At physical completeness that matrix has a
zero top row, which does not invalidate (3) or select an
arbitrary value for the original zero vacuum arrow.

The generic classical meridian has \(x=-M\). M's actual
factorial-basis symbols are
\[
 K=-M/A,\qquad
 e=(M/A-M^{-1})p_{\rm new}
                  =-(K+M^{-1})p_{\rm new}.
 \tag{5}
\]
The unilateral coupon has symbol \(-p_{\rm new}\).
Thus (3) is compatible with the selected classical flag
ratio on every regular \(M\)-chart where \(K+M^{-1}\)
is a unit, not just at \(M=1\).
Only the displayed row is asserted: it is not a proof of
a full quantum auxiliary eigenvector, Hopf intertwiner,
or braid-covariant flag.

## 2. Exact oscillator and endpoint identities

Let \(A_{\rm occ}e_a=Q^a e_a\), let \(P_d=e_{N-1}e_{N-1}^*\),
and put \(\delta=1-Q^N\), \(\rho=q-q^{-1}\). Directly from
(1)--(2),
\[
 FQ_{\rm f}=-q^{-1}(I-A_{\rm occ}),\qquad
 Q_{\rm f}F=-q^{-1}(I-QA_{\rm occ})+q^{-1}\delta P_d .
 \tag{6}
\]
For the second equality the displayed diagonal expression
at \(a=N-1\) is corrected to the actual value zero.
Consequently
\[
 \boxed{\quad
 Q_{\rm f}F-QFQ_{\rm f}
                  =\rho I+q^{-1}(1-Q^N)P_d ,
 \quad}
 \tag{7}
\]
\[
 Q_{\rm f}F=-q^{-1}I-MK^{-1}+q^{-1}(1-Q^N)P_d .
 \tag{8}
\]
These are identities for the actual truncated matrices.
At a physical root the coefficient \(\delta\) is zero,
but its ordinary \(q\)-derivatives need not be. The full
last term of (7)--(8) precedes every parameter derivative.
No cyclic wrap is substituted for the unilateral coupon.

This is already enough to distinguish (1) from an unmarked
module endomorphism: \(KQ_{\rm f}=Q Q_{\rm f}K\), so at
the physical roots it does not commute with \(K\), for every \(N\ge2\).
Its source use is as a specified coupon, with the marked
defect retained, rather than as an automatically available
Casimir polynomial.

## 3. The routed degree-zero coordinate and its collars

Use the same reference constants \(c\ne0,d\), initial
meridian head \(j\), and exact ordered matrices
\(\widehat\mu_j\) as C and B. Define
\[
 \boxed{\quad
 T_{\rm f}=
   \frac{\widehat\mu_{j,11}
                       +Q_{{\rm f},1}\widehat\mu_{j,21}-dI}{c}.
 \quad}
 \tag{9}
\]
The first meridian entry has total occupation degree zero,
and the second has degree \(+1\), by C's prefix formulas.
Since \(Q_{{\rm f},1}\) has degree \(-1\), \(T_{\rm f}\)
has degree zero exactly. Its principal expression is
\[
              \tau_{\rm f}
                  =(\mu_{j,11}-p_{\rm new}\mu_{j,21}-d)/c .
 \tag{10}
\]
Common momentum scaling multiplies \(p_{\rm new}\) and
the upper-right meridian entries by \(\lambda\), and the
lower-left entries by \(\lambda^{-1}\), leaving diagonal
entries fixed. Hence (10) is invariant.
At \(M=1\), on the fixed reference framing family and
the chosen \(p_{\rm new}=1\) slice, B identifies (10) with
\(t=r/s\), and the actual principal Ward field has
\(\mathscr V\tau_{\rm f}=1\). These statements remain
restricted to that fixed reference family and its common
momentum orbit; they are not assertions at every representation.

The inverse-free formula improves the insertion's parameter
domain. Fix small \(\eta>0\), independently of \(N\), and set
\[
        |q-q_N|\le\eta/N,\qquad |M-1|\le\eta,
                \qquad q_N=e^{\pi i/N}.
 \tag{11}
\]
Choose \(\eta<1/4\). On this bidisk \(q,M\) are nonzero.
For all integer \(|m|\le C_bN\),
\[
                         |q^m|\le C_{b,\eta}.
 \tag{12}
\]
Indeed \(|\log|q||\le C\eta/N\), so the modulus of the
power is at most \(e^{CC_b\eta}\).
The entries of \(K_i^{\pm1},\mathcal E_i,F_i\) are therefore
bounded independently of \(N\), with their original zero
arrows. Also \(\|Q_{\rm f}\|_{\rm row}=|q|^{-1}\).
The fixed ordered prefix contains only a fixed number of
these factors and their \(K\) inverses. Thus
\[
                       \|T_{\rm f}\|_{\rm row}\le C_j
 \tag{13}
\]
on (11), retaining the fixed \(c,d\).
On the half bidisk, matrix Cauchy estimates yield
\[
 \|\partial_q^u\partial_M^vT_{\rm f}\|_{\rm row}
 \le C_j\,u!v!(2N/\eta)^u(2/\eta)^v.
 \tag{14}
\]
This uses the row-sum operator norm and inserts no tensor
dimension factor.

On the genuine finite-color path \(M=-q^N\), a sufficiently
small disk \(|q-q_N|\le\eta'/N\) lies in a bidisk of the
form (11), since \(|q^N-q_N^N|\le C N|q-q_N|\).
Consequently the whole insertion on that path has
\[
         \left\|\frac{d^k}{dq^k}T_{\rm f}(q,-q^N)
               \right\|_{\rm row}\le C_j k!(C N)^k
 \tag{15}
\]
on a smaller such disk. These are insertion bounds.
They do not estimate the original word, its scalar
contraction, or a boundary current paired with that word.

## 4. Exact comparison with the previous bounded mark

On B's smaller bidisk, its matrix
\(\widehat Q=(K_1+I)^{-1}\mathcal E_1\) is defined.
Combining it with (3) gives the exact ordered difference
\[
 \widehat Q-Q_{{\rm f},1}
       =(qM^{-1}-1)(K_1+I)^{-1}Q_{{\rm f},1},
 \tag{16}
\]
\[
 \Delta T:=T_{\rm bal}-T_{\rm f}
       =\frac{qM^{-1}-1}{c}
          (K_1+I)^{-1}Q_{{\rm f},1}\widehat\mu_{j,21}.
 \tag{17}
\]
At \(M=1,q=q_N\), the shift coefficient of (16) on
input \(a>0\) is
\[
                  \frac{q^{-1}-1}{1-q^{1-2a}}.
 \tag{18}
\]
It is \(O(N^{-1})\) when \(a/N\) stays in a fixed compact
subinterval of \((0,1)\), but at \(a=1\) it equals \(-1\)
exactly. Thus the endpoint comparison is genuinely of
order one, despite equality of the regular principal
symbols. B's whole normals apply to (16)--(17) on its
smaller bidisk; no endpoint replacement by zero is justified.

For any original source, linearity gives the exact difference
\(\Phi_O(\Delta T\,B_0)\), with \(B_0\) denoting an arbitrary
insertion. Its product-current correction is explicit:
\[
 [\mathcal D_N,M_{T_{\rm bal}}]
       -[\mathcal D_N,M_{T_{\rm f}}]
                    =[\mathcal D_N,M_{\Delta T}].
 \tag{19}
\]
For powers one retains every noncommutative term,
\[
 T_{\rm bal}^k-T_{\rm f}^k
   =\sum_{\ell=0}^{k-1}
       T_{\rm bal}^{\ell}\Delta T\,T_{\rm f}^{\,k-1-\ell}.
 \tag{20}
\]
If both resolvents exist, the exact comparison is
\[
 R_{\rm bal}(\zeta)-R_{\rm f}(\zeta)
                =R_{\rm bal}(\zeta)\Delta T\,R_{\rm f}(\zeta).
 \tag{21}
\]
These identities compare the same original source; they
do not reset a cut or a transported marked coupon.

## 5. Actual operator-valued Jacobi rows

Remove the first prefix factor in C's exact meridian:
\[
 \widehat\mu_j=\widehat b_{-,1}^{-1}
                       \overline\mu_j\widehat b_{-,1},
 \qquad
 \overline\mu_j=
       \begin{pmatrix}\overline A&\overline B\\
                       \overline C&\overline D\end{pmatrix}.
 \tag{22}
\]
The entries of \(\overline\mu_j\) act only on heads \(2,\ldots,j\).
They keep the physical minus sign and all remaining prefixes.
They commute with the first-head matrices, but are not
assumed to commute with one another.

Multiplying
\(\widehat b_{-,1}=\left(\begin{smallmatrix}I&0\\-KF&K\end{smallmatrix}\right)\)
and its exact inverse
\(\left(\begin{smallmatrix}I&0\\F&K^{-1}\end{smallmatrix}\right)\)
gives
\[
 \begin{split}
 \widehat\mu_{j,11}&=\overline A-KF\overline B,\\
 \widehat\mu_{j,21}&=F\overline A-FKF\overline B
                                +K^{-1}\overline C-F\overline D .
 \end{split}
 \tag{23}
\]
Therefore the numerator \(Z_{\rm f}=cT_{\rm f}+dI\) is
\[
 \boxed{\begin{split}
 Z_{\rm f}={}&(I+Q_{\rm f}F)\overline A
                 -(Q_{\rm f}F)\overline D\\
        &-(I+Q_{\rm f}F)KF\overline B
                      +Q_{\rm f}K^{-1}\overline C .
 \end{split}}
 \tag{24}
\]
This is an exact operator-valued tridiagonal matrix in the
first occupation.

For explicit rows put \(k_a=-M q^{-1}Q^{-a}\), and
\[
 d_a=-q^{-1}(1-Q^{a+1})\quad(a<N-1),\qquad d_{N-1}=0.
 \tag{25}
\]
The diagonal block of \(Z_{\rm f}\) at \(a\) is
\[
                    (1+d_a)\overline A-d_a\overline D.
 \tag{26}
\]
Its block from input \(a\) to output \(a+1\), for \(a<N-1\), is
\[
       -(1+d_{a+1})k_{a+1}(1-Q^{a+1})\overline B.
 \tag{27}
\]
Its block from input \(a\) to output \(a-1\), for \(a>0\), is
\[
                         -q^{-1}k_a^{-1}\overline C.
 \tag{28}
\]
All other blocks are zero. The two missing endpoint blocks
are zero, not cyclic. To obtain \(T_{\rm f}\), subtract
\(dI\) on the diagonal and divide every block by \(c\).

Equations (24)--(28) preserve the full finite source and
its normal walls (7)--(8). No division by \(\overline B\)
or \(\overline C\) is made. The remaining operator blocks
and the cut/marked environment are still unknown contractions.
Thus these equations provide an actual Jacobi-row reduction,
not a scalar orthogonal-polynomial spectral identification.
The old affine clock spectrum is not transferred to this mark.

## 6. All sourced current rows remain

Keep C/B's actual operator and source:
\[
 \mathcal D_N(B_0)=h^{-1}\sum_\iota[X_\iota,A_\iota B_0],
 \qquad \Phi_O(B_0)=\varkappa_\beta\operatorname{Tr}(PB_0O).
 \tag{29}
\]
Write its complete boundary as
\[
 \mathcal C_P(B_0,O)=\frac{\varkappa_\beta}{h}
   \sum_\iota\left\{
    \operatorname{Tr}([P,X_\iota]A_\iota B_0O)
       +\operatorname{Tr}(PA_\iota B_0[O,X_\iota])\right\}.
 \tag{30}
\]
Define
\[
 \mathcal A_N^{\rm f}
              =[\mathcal D_N,M_{T_{\rm f}}]-\operatorname{Id}.
 \tag{31}
\]
It has zero principal restriction on the fixed complete
reference family, but no small whole-source norm is asserted.
Its exact matrix formula is
\[
 [\mathcal D_N,M_{T_{\rm f}}](B_0)
   =h^{-1}\sum_\iota\left\{
       [X_\iota,T_{\rm f}]A_\iota B_0
       +[X_\iota,[A_\iota,T_{\rm f}]B_0]\right\}.
 \tag{32}
\]
For a polynomial \(p\), form \(\mathcal A_{N,p}^{\rm f}\)
by the full ordered sum in B, with \(T_{\rm f}\) replacing
\(T_{\rm bal}\). Then
\[
 \Phi_O(p'(T_{\rm f})B_0)
   =\mathcal C_P(p(T_{\rm f})B_0,O)
       -\Phi_O(p(T_{\rm f})\mathcal D_N(B_0))
       -\Phi_O(\mathcal A_{N,p}^{\rm f}(B_0)).
 \tag{33}
\]
Every cut and tail-pivot commutator, all
\([O,X_\iota]\), and \(\mathcal D_N(I)\) remain.
All formulas can be differentiated as whole finite arrays
on the genuine parameter paths, including the top wall.

The bound (13) gives a fixed exterior circle for
\(R_{\rm f}(\zeta)=(\zeta I-T_{\rm f})^{-1}\) and the
uniform estimate
\(\|R_{\rm f}(\zeta)\|_{\rm row}\le(|\zeta|-C_j)^{-1}\).
The exact marked resolvent current is
\[
 \begin{split}
 \partial_\zeta\Phi_O(R_{\rm f}B_0)
    ={}&-\mathcal C_P(R_{\rm f}B_0,O)
        +\Phi_O(R_{\rm f}\mathcal D_N(B_0))\\
       &+\Phi_O\big(R_{\rm f}
                      \mathcal A_N^{\rm f}(R_{\rm f}B_0)\big).
 \end{split}
 \tag{34}
\]
It follows from
\([\mathcal D_N,M_{R_{\rm f}}]+\partial_\zeta M_{R_{\rm f}}
=M_{R_{\rm f}}\mathcal A_N^{\rm f}M_{R_{\rm f}}\).
The anomaly acts on the entire \(R_{\rm f}B_0\).

The finite Jacobi rows, bounded coupon, and exterior
resolvent do not construct the original relative framing
cycle. They retain an exact source on which that comparison
can be attempted. They do not supply a period normalization,
a nonzero geometric coefficient, or an estimate of the
unrestricted exterior paired with their endpoint currents.

## Complete proof-source pins

* C: notes/research_actual_routed_centralizer_coordinate.md,
  SHA256 6bc8e8438646ad713d3951f072259cfd8844a13e97c844601b2eca11a9497033.
* B: notes/research_actual_balanced_routed_framing_coordinate.md,
  SHA256 56b6a30116551df89f56b261965d0641991bae746c8aa3649db73d7295e2d6cb.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

All three complete texts were freshly read in the active
author sequence and retained unchanged. Their actual
matrices, signs, prefix order, generic meridian symbols,
source currents, and normal-path conventions were checked.
All additional statements are proved here by finite
matrix algebra and uniform elementary bounds.
No frozen or public file was changed.
