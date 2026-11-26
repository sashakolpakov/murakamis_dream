# The finite clock spectrum and resolvent current of the routed framing coordinate

Private written proof, 18 November 2026.

The actual routed insertion of C has \(N\) affine clock eigenvalues.
Its resolvent has pole order at most \(j(N-1)+1\), where \(j\) is the
chosen routed head, rather than the dimension \(N^b\) of the full
tensor space. The bound holds in the genuine parameter germ, before
root specialization. The resulting one-variable marked source
satisfies an exact differential identity retaining the original
cut, pivotal, marked-word, and Ward correction currents.

These facts give an actual finite spectral model for a coordinate
whose restricted principal value is \(r/s\). They do not identify
its spectral contour with the geometric relative framing chain.
In particular, the number of poles and the factor \(N\) in the
power-current identity below do not determine their source weights.

The complete proof directs are C for the routed insertion and current,
W for the ordered Ward coefficients, and M for the literal crossing
support, pinned at the end. All additional matrix, filtration, and
resolvent calculations are proved here.

## 1. Ordered prefix and occupation filtrations

Keep C's \(b\) original heads of dimension \(N\), its zero endpoint
arrows, its parameter \(x=-M/q\), and \(Q=q^2\). The fixed reference
meridian has entries \(a,b_0,c,d\), with \(c\ne0\). In particular
\(c,d\) below are fixed reference constants, not occupation indices.
The chosen head is \(j\). Write the routed insertion as
\[
 T=\frac{\widehat\mu_{j,11}-\widehat\mu_{j,21}-dI}{c},
 \qquad Z=cT+dI.
 \tag{1}
\]
Only heads \(1,\ldots,j\) occur in \(T\); the remaining heads are
spectators. All formulas use the order specified in C.

Put
\[
 K_p=K_{j-1}\cdots K_1,\qquad
 F_p=F_1+K_1^{-1}F_2+\cdots+
                         K_1^{-1}\cdots K_{j-2}^{-1}F_{j-1}.
 \tag{2}
\]
For an empty prefix use \(K_p=I,F_p=0\). Direct multiplication of
the lower triangular matrices of C gives
\[
 \widehat B_{j-1}=
       \begin{pmatrix}I&0\\-K_pF_p&K_p\end{pmatrix},
 \qquad
 \widehat B_{j-1}^{-1}=
       \begin{pmatrix}I&0\\F_p&K_p^{-1}\end{pmatrix}.
 \tag{3}
\]
For example, adjoining head \(l\) replaces \(F_p\) by
\(F_p+K_p^{-1}F_l\), which proves (2)--(3) inductively.
No \(K_i\) is commuted past its own \(F_i\).

Set
\[
 A=\widehat\mu_{j,11}=-K_j+\mathcal E_jK_pF_p,
 \tag{4}
\]
\[
 C_1=\widehat\mu_{j,21}
   =F_pA-K_p^{-1}K_jF_j+
                              (K_j^{-1}+\mathcal E_jF_j)F_p .
 \tag{5}
\]
These are obtained by multiplying the three matrices in C's
\(-\widehat B_{j-1}^{-1}\widehat G_j\widehat B_{j-1}\).
Thus \(Z=A-C_1\). The physical minus sign is included in (4)--(5).

Let the total occupation on the routed heads be
\[
                          L=a_1+\cdots+a_j .
 \tag{6}
\]
The matrix \(A\) preserves \(L\). Its off-diagonal part lowers
\(a_j\) by one and raises the prefix occupation by one.
Every term of \(C_1\) raises \(L\) by exactly one, or is zero at
an actual endpoint. This follows term by term from (5):
\(F_p\) and \(F_j\) raise one occupation, while
\(\mathcal E_jF_j\) has degree zero. No continued arrow outside
the finite head is used.

Order the tensor basis first by \(L\), and within one \(L\) by
the head-\(j\) occupation in the direction making its lowering
term triangular. Equations (4)--(5) show that \(T\) is triangular
in this order. Its diagonal entries are
\[
                \lambda_a=\frac{-xQ^{-a}-d}{c},
                   \qquad 0\le a<N.
 \tag{7}
\]
Each value occurs \(N^{b-1}\) times, counting all other heads.
Consequently, for every parameter value for which the matrices
are defined,
\[
 \det(\zeta I-T)
  =c^{-N^b}
       \left[\prod_{a=0}^{N-1}(c\zeta+d+xQ^{-a})\right]^{N^{b-1}}.
 \tag{8}
\]
This is a characteristic-polynomial identity, not a claim of
diagonalizability.

## 2. A nilpotent bound valid before specialization

Define
\[
 P_{N,q}(y)=\prod_{a=0}^{N-1}(y+xQ^{-a}),\qquad
 p_{N,q}(\zeta)=P_{N,q}(c\zeta+d),
 \qquad \nu=j(N-1)+1.
 \tag{9}
\]
The filtration by \(a_j\le a\) proves
\[
                           P_{N,q}(A)=0.
 \tag{10}
\]
Indeed, \(A+xQ^{-a}I\) sends the subspace \(a_j\le a\)
into \(a_j\le a-1\). Start with \(a=N-1\) and apply these
factors down to \(a=0\). The factors are polynomials in \(A\)
and commute, so their product is exactly (10). This argument
does not require \(Q\) to be a root of unity or the values in
(7) to be distinct.

Expand \(P_{N,q}(A-C_1)-P_{N,q}(A)\) in noncommutative words.
Every surviving word contains at least one \(C_1\). By (6),
it strictly raises total routed occupation. Therefore
\[
 H_N:=p_{N,q}(T)=P_{N,q}(Z)
 \quad\hbox{strictly raises }L,
 \qquad
 \boxed{\quad H_N^\nu=0.\quad}
 \tag{11}
\]
The maximum \(L\) is \(j(N-1)\), proving the displayed exponent.
Spectator heads do not enlarge it.

At the physical root \(q=e^{\pi i/N}\), \(Q\) is primitive and
\[
 P_{N,q}(y)=y^N-(-x)^N,\qquad
 H_N=(cT+dI)^N-(-x)^N I .
 \tag{12}
\]
For the complete value \(M=1\), \((-x)^N=q^{-N}=-1\).
Thus the affine clock eigenvalues obey
\[
                          (c\lambda_a+d)^N=-1.
 \tag{13}
\]
Equations (10)--(11), rather than a differentiation of the
root-only formula (12), will be used for genuine normals.

There is also an explicit diagonalizer for the occupation-preserving
part. Put
\[
 Y=K_j^{-1}\mathcal E_jK_pF_p,\qquad
 \mathcal U_N=
 \sum_{n=0}^{N-1}
        \frac{Q^nY^n}{\prod_{r=1}^n(1-Q^r)} .
 \tag{13a}
\]
Here \(Y^N=0\): every factor lowers the head-\(j\) occupation,
and the actual vacuum arrow is zero. Also \(K_jY=QYK_j\).
All denominators in (13a) are nonzero at the physical root,
and on a sufficiently small genuine parameter germ. The constant
term of \(\mathcal U_N\) is \(I\), so it is invertible by a finite
nilpotent series. Its coefficients give
\[
 \mathcal U_N(Y)=(1-Y)\mathcal U_N(Q^{-1}Y).
 \tag{13b}
\]
Indeed, for \(1\le n<N\) the coefficient recurrence is
\[
 u_n(1-Q^{-n})=-Q^{-(n-1)}u_{n-1};
\]
the possible degree \(N\) remainder vanishes because \(Y^N=0\).
Since \(A=-K_j(1-Y)\), (13b) implies
\[
                  A=\mathcal U_N^{-1}(-K_j)\mathcal U_N.
 \tag{13c}
\]
This is an exact finite conjugation, with its own retained
coefficients. It is not identified with a braid crossing or
with an unchanged source. No norm bound for \(\mathcal U_N\)
or its inverse is asserted.

## 3. Resolvent poles, jets, and source residues

Let
\[
                         R_N(\zeta)=(\zeta I-T)^{-1}.
 \tag{14}
\]
The annihilating polynomial \(p_{N,q}^\nu\) from (11) gives
an explicit rational expression for (14). If
\(m(\zeta)=p_{N,q}(\zeta)^\nu\), then
\[
 R_N(\zeta)=
 \frac{m(\zeta)I-m(T)}{m(\zeta)(\zeta I-T)}
 =\frac{\mathcal Q(\zeta,T)}{m(\zeta)},
 \tag{15}
\]
where \(\mathcal Q\) is the polynomial divided difference of
\(m\); \(m(T)=0\). Thus the only possible poles are (7).
Near the physical root these \(N\) values are distinct.
Every matrix pole has order at most \(\nu\).

All entries of the divided difference and of \(p_{N,q}\)
are holomorphic in a sufficiently small fixed-\(N\) parameter
germ with \(q,M,c\ne0\). A parameter derivative of total order
\(k\) in (15) has denominator dividing \(p_{N,q}^{\nu+k}\).
Because its roots remain simple on that germ, its pole order
at each moving clock is at most \(\nu+k\). An additional
\(\ell\) derivatives in \(\zeta\) increase this to at most
\(\nu+k+\ell\). These are algebraic pole-order bounds, not
uniform estimates for residues or for the size of that germ.
They apply in particular on the ordinary quantum path
\(M=-q^N\), with the head size \(N\) fixed.

For completeness, the partial fractions have the form
\[
 R_N(\zeta)=
 \sum_{a=0}^{N-1}\sum_{l=0}^{\nu-1}
       \frac{(T-\lambda_a I)^l\Pi_a}{(\zeta-\lambda_a)^{l+1}},
 \tag{16}
\]
where \(\Pi_a\) is the spectral projector onto the generalized
\(\lambda_a\)-space. This follows either by division of (15)
at each distinct root or by the coprimality of the factors
\((\zeta-\lambda_a)^\nu\). In particular
\(\sum_a\Pi_a=I\) and
\((T-\lambda_a I)^\nu\Pi_a=0\).

Keep C's original functional
\[
             \Phi_O(B)=\varkappa_\beta\operatorname{Tr}(PBO),
 \tag{17}
\]
including the full cut, pivots, peripheral scalar, and marked
word. Define the actual one-variable source
\[
                  \mathcal L_{N,B,O}(\zeta)
                         =\Phi_O(R_N(\zeta)B).
 \tag{18}
\]
Its Laurent coefficients are the finite routed insertions
\[
        \ell_{a,l}=
                  \Phi_O((T-\lambda_a I)^l\Pi_a B).
 \tag{19}
\]
They may vanish or cancel. The scalar source can have fewer
poles than the matrix resolvent.

For a positively oriented contour \(\Gamma\) enclosing all
clock poles, and no other singularities of the displayed
rational function,
\[
 \frac1{2\pi i}\int_\Gamma\mathcal L_{N,B,O}(\zeta)\,d\zeta
       =\sum_a\ell_{a,0}=\Phi_O(B),
 \tag{20}
\]
\[
 \frac1{2\pi i}\int_\Gamma
                  f(\zeta)\mathcal L_{N,B,O}(\zeta)\,d\zeta
                        =\Phi_O(f(T)B)
 \tag{21}
\]
for every polynomial \(f\). These follow by expanding the
resolvent at infinity, or directly from (16). A common fixed
contour works on a sufficiently small parameter germ, so the
whole identities may be differentiated there. The derivatives
of \(P,O,B,\varkappa_\beta,T\) are all retained.

## 4. Exact source-band reduction and simple unmarked poles

Let total degree now mean total occupation on all \(b\) heads.
An operator has degree \(\delta\) if it shifts that integer
by \(\delta\), with every endpoint arrow still truncated.
Write
\[
 T=T^{(0)}+T^{(+)},\qquad
 T^{(0)}=(A-dI)/c,\qquad T^{(+)}=-C_1/c,
 \quad R_0(\zeta)=(\zeta I-T^{(0)})^{-1}.
 \tag{21a}
\]
Their degrees are respectively zero and \(+1\). Since \(R_0\)
also preserves occupation on the routed heads, the finite
nilpotent resolvent expansion is
\[
 R_N(\zeta)=
 \sum_{k=0}^{j(N-1)}(R_0(\zeta)T^{(+)})^kR_0(\zeta).
 \tag{21b}
\]
It follows by factoring
\(\zeta I-T=(\zeta I-T^{(0)})(I-R_0T^{(+)})\).
Every term of the sum has degree \(k\).

Suppose \(P\) is the prescribed diagonal cut/pivot matrix and
\(B,O\) are homogeneous with combined degree \(\delta\).
The trace of an operator of nonzero degree is zero. Hence (18)
is zero for \(\delta>0\), and for \(\delta=-k\le0\) it is exactly
\[
 \mathcal L_{N,B,O}(\zeta)
   =\Phi_O\big((R_0T^{(+)})^kR_0B\big).
 \tag{21c}
\]
It is zero also if \(k>j(N-1)\).
By (10), or (13c), \(R_0\) has only simple poles when the
clock eigenvalues are distinct. Thus (21c) has pole order
at most \(k+1\). This is a source-band bound, which can be
much smaller than the matrix bound \(\nu\).
An arbitrary finite array is treated by its exact degree
decomposition; a fixed finite collection of charged insertion
bands retains a bound independent of \(N\).

In particular, when \(B,O\) have degree zero,
\[
 \mathcal L_{N,B,O}(\zeta)=\Phi_O(R_0(\zeta)B)
       =\sum_{a=0}^{N-1}\frac{w_a}{\zeta-\lambda_a},
 \tag{21d}
\]
\[
 w_a=\varkappa_\beta\operatorname{Tr}
  \big(P\mathcal U_N^{-1}T_a^{(j)}\mathcal U_NBO\big),
 \qquad \sum_aw_a=\Phi_O(B).
 \tag{21e}
\]
Here \(T_a^{(j)}\) is the literal diagonal head-\(j\) projector,
with identities on the other heads. Equation (13c) proves
(21e), including the order of all source factors.
Neither positivity nor nonvanishing of these weights is claimed.

This applies to the original unmarked braid word and its
diagonal occupation-clock marks. M's exact positive crossing
sends \((a,b)\) to \((b+n,a-n)\), and its negative crossing
sends \((a,b)\) to \((b-n,a+n)\). Both preserve the integer
sum of the two occupations, including their finite support.
Consequently every literal crossing word, diagonal pivot,
and diagonal clock preserves total degree. The statement
uses integer occupation, not just its residue modulo \(N\).
The same support holds throughout the genuine ordinary
parameter germ, so it survives every parameter derivative.
Charged coupons instead use (21c) or the general finite
band decomposition; they are not silently projected away.

For example, the degree-zero source obeys
\[
          \Phi_O\big(p_{N,q}(T)f(T)B\big)=0
 \tag{21f}
\]
for every polynomial \(f\). The first factor strictly raises
occupation and the second has only nonnegative degrees.
This is a source identity, not the matrix equation
\(p_{N,q}(T)=0\). Normal derivatives of (21d)--(21f)
retain their exact cancellations; moving simple poles in
(21d) can have normal jets of order at most \(k+1\)
after \(k\) parameter derivatives.

## 5. The exact resolvent Ward equation

Use C's divergence-form superoperator and its exact anomaly:
\[
 \mathcal D_N(B)=h^{-1}\sum_\iota[X_\iota,A_\iota B],
 \qquad
 \mathcal A_N=[\mathcal D_N,M_T]-\operatorname{Id}.
 \tag{22}
\]
Here \(M_T\) is left multiplication. The scalar parameter
\(\zeta\) is external to \(\mathcal D_N\). Inverting the
superoperator \(M_{\zeta I-T}\) gives
\[
 [\mathcal D_N,M_{R_N}]
   =M_{R_N}[\mathcal D_N,M_T]M_{R_N}
   =M_{R_N^2}+M_{R_N}\mathcal A_N M_{R_N}.
 \tag{23}
\]
Since \(\partial_\zeta R_N=-R_N^2\), this is equivalently
\[
 [\mathcal D_N,M_{R_N}]+\partial_\zeta M_{R_N}
                      =M_{R_N}\mathcal A_N M_{R_N}.
 \tag{24}
\]
The signs follow from
\([D,L^{-1}]=-L^{-1}[D,L]L^{-1}\) with
\([D,M_{\zeta I-T}]=-[D,M_T]\).

C's full sourced boundary current is
\[
 \mathcal C_P(B,O)=\frac{\varkappa_\beta}{h}
 \sum_\iota\left\{
  \operatorname{Tr}([P,X_\iota]A_\iota BO)
  +\operatorname{Tr}(PA_\iota B[O,X_\iota])
                         \right\},
 \quad
 \Phi_O(\mathcal D_N B)=\mathcal C_P(B,O).
 \tag{25}
\]
Apply (24) to \(B\) and then apply \(\Phi_O\). The result is
the exact meromorphic differential identity
\[
 \boxed{\begin{split}
 \partial_\zeta\mathcal L_{N,B,O}
    ={}&-\mathcal C_P(R_N B,O)
       +\Phi_O(R_N\mathcal D_N(B))\\
       &+\Phi_O\big(R_N\mathcal A_N(R_N B)\big).
 \end{split}}
 \tag{26}
\]
In particular the correction acts on the whole \(R_N B\);
it is not multiplication by a scalar error.
Also \(\mathcal D_N(I)\) need not vanish. Every marked-word
commutator and every cut or tail-pivot commutator in (25)
remains in (26).

This identity is valid for the actual finite arrays and all
parameters where they are defined, and meromorphically in
\(\zeta\). It is not obtained by replacing the source by a
cyclic trace or by its principal framing restriction.

The degree reductions are compatible with the full Ward current.
To check this directly from W, its matrices have degrees
\[
 \deg X_E=-1,\quad \deg X_F=1,\quad \deg X_K=0,
 \qquad
 \deg A_E=1,\quad \deg A_F=-1,\quad \deg A_K=0.
 \tag{26a}
\]
Indeed \(\widehat c=K_1F_1\), \(\widehat b=\mathcal E_1\),
and \(2\widehat a=K_1-K_1^{-1}-\mathcal E_1F_1\);
W defines \(A_E=\widehat c\,\mathsf K^{-1}\),
\(A_F=\widehat b\), and
\(A_K=(2\widehat a+\widehat b\,\mathsf F)\mathsf K^{-1}\).
Thus \(\mathcal D_N\) preserves each degree. This verifies
compatibility without omitting its divergence term.
All currents in (26) may consequently be sorted into their
actual degree bands before taking the diagonal source trace.

## 6. Exterior principal symbol and the exact power current

There is a direct region in which (18) is a resolvent mark
for the actual principal coordinate, without a uniform
resolvent assumption near its growing spectral set.
Fix a compact regular interior phase chart and bounded
logarithmic momenta. At the physical roots, all entries of
the finite shifts \(K_i^{\pm1},\mathcal E_i,F_i\) are uniformly
bounded on the full heads. Conjugating by the corresponding
exponential occupation weights multiplies each fixed shift
by a bounded factor. Formulas (2), (4), and (5) contain a
fixed number of such shifts. Their weighted row-sum norms
therefore give
\[
                             \|T\|_{\rm row}\le C_*
 \tag{27}
\]
uniformly in \(N\) on that compact set. The same assertion
holds on a small ordinary parameter collar with
\(|q-q_N|=O(N^{-2})\), where \(M=-q^N\), if such normals
are considered; only boundedness is claimed here.

For \(|\zeta|>C_*\), the finite-matrix Neumann series converges normally:
\[
                   R_N(\zeta)=
                   \sum_{k\ge0}\frac{T^k}{\zeta^{k+1}}.
 \tag{28}
\]
On an interior sequence of occupation rows, each fixed \(k\)
sees no endpoint once \(N\) is large. C's principal symbol
rule then gives the symbol \(\tau^k\) for that term.
The uniform geometric bound in (27)--(28) permits passage
to the limit term by term, for example by first truncating
at \(k=K\) and then bounding the remaining tail uniformly.
Thus the leading interior symbol is
\[
                              \frac1{\zeta-\tau}.
 \tag{29}
\]
This proves the leading identification on the actual interior
rows in the exterior domain. Its regular symbol is the rational
expression (29), whose continuation to C's complex reference
framing family is \(1/(\zeta-r/s)\). This last identification
is the continued principal expression; no uniform complex
coherent-kernel estimate is asserted. Nor is there a uniform
analytic resolvent assertion through the finite clock spectrum.
Likewise C's anomaly has vanishing principal restriction only
on that reference family.

At the root, the polynomial \(H_N\) of (12) has an additional
exact current identity. From
\([\mathcal D_N,M_Z]=c(\operatorname{Id}+\mathcal A_N)\),
\[
 [\mathcal D_N,M_{H_N}]
       =Nc\,M_{Z^{N-1}}+\mathcal B_N,
 \qquad
 \mathcal B_N=
 c\sum_{\ell=0}^{N-1}
          M_Z^\ell\mathcal A_N M_Z^{N-1-\ell}.
 \tag{30}
\]
Consequently
\[
 \boxed{\quad
 Nc\,\Phi_O(Z^{N-1}B)
   =\mathcal C_P(H_NB,O)
      -\Phi_O(H_N\mathcal D_N(B))
      -\Phi_O(\mathcal B_N(B)).
 \quad}
 \tag{31}
\]
This retains the nilpotent \(H_N\), which is not assumed zero.
The degree \(N\) correction \(\mathcal B_N\) has no uniform
bound supplied by a fixed-degree principal symbol statement.
For genuine parameter derivatives one uses the general
polynomial \(p_{N,q}\) in (9), its full derivative current,
and then specializes; one does not differentiate (12) as an
identity away from the root.

There is an important exact constraint in the degree-zero
source. If \(B,O\) have degree zero, both of the first two
terms on the right of (31) vanish: \(H_NB\) strictly raises
occupation, \(\mathcal D_N\) preserves it, and (25) expresses
the first current as that same vanishing source trace.
Therefore
\[
              \Phi_O(\mathcal B_N(B))
                        =-Nc\,\Phi_O(Z^{N-1}B).
 \tag{31a}
\]
The factor \(N\) is thus accompanied by an exact sourced
anomaly contribution. Deleting that contribution would
already violate the original finite identity.

## 7. The new reduction and its remaining comparison

Equations (7), (11), (18), and (26) give a specified
one-variable marked source, with \(N\) explicit clock
locations, linear-in-\(N\) pole-order bound, and exact
cut/current/anomaly transport. Equations (20)--(21)
recover the original source and every polynomial routed
moment from this model. Equation (31) records an actual
factor \(N\) in its power-current relation.

The contour in (20) is a finite spectral Cauchy contour.
No equality with the geometric normal pushforward of the
original relative filling chain has been proved. Its
residue coefficients still depend on the original source.
In particular, neither the \(N\) clock locations nor (31)
implies an \(N\)-fold geometric framing path, a nonzero
effective endpoint sum, or an exponential lower bound.
Such conclusions require control of (25)--(26), including
their same-action endpoint and anomaly terms.

## Complete proof-source pins

* C: notes/research_actual_routed_centralizer_coordinate.md,
  SHA256 6bc8e8438646ad713d3951f072259cfd8844a13e97c844601b2eca11a9497033.
* W: notes/research_actual_weighted_ward_centralizer_lift.md,
  SHA256 e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

All three complete directs were freshly read nontruncated in
this author sequence. Their finite matrices and prefix order,
restricted principal coordinate, full sourced current,
literal crossing support, and genuine-normal qualifications
were checked. All further
identities above are explicit finite algebra or written
filtration and convergence arguments. No frozen or public
file was changed.
