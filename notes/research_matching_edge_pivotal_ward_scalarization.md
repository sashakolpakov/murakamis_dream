# The marked matching block as a scalar Hermite pairing

21 November 2026. Research note; previous final notes and public
manuscripts remain unchanged.

The completed matching-edge operator can be contracted with its actual
ordinary exterior before estimating its projectors or their moving-parameter
derivatives. The result is an exact scalar pairing with the value and
nilpotent coefficient of a regular exterior intertwiner. In particular,
the first normal required by the original physical mark can be evaluated
from root data, without separate norms of moving spectral projectors.

A pivotal turn has to be treated carefully. Its transpose on all matrix
arrays contains an extra clock and generally does not preserve
intertwiners. We prove the all-array identity first. A partial trace then
removes that clock on an entire intertwiner family. Only after this
replacement do we differentiate. No claim is made that the original
exterior annihilates an isolated projector derivative.

The scalar exterior coefficients below can still have exponential size
and can still cancel. This note supplies no new volume identity or
finite-exception theorem.

## 1. The actual physical slot and its ordinary exterior

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and let
\(\zeta=q e^t\). Put \(Q=\zeta^2\) and
\(F_j=(Q;Q)_j=\prod_{r=1}^j(1-Q^r)\), with \(F_0=1\). Write
\([j]_\zeta=(\zeta^j-\zeta^{-j})/(\zeta-\zeta^{-1})\).
On the physical highest-weight-\(d\) space \(V\),
use the original balanced generators and physical cup:
\[
 \begin{split}
 F|u\rangle&=(1-Q^{u+1})|u+1\rangle,\\
 \mathcal E|u\rangle&=\zeta^{-N}(1-Q^{N-u})|u-1\rangle,\\
 K|u\rangle&=K_u|u\rangle,
                 \qquad K_u=\zeta^{d-2u},\\
 p_{u,d-u}&=p_u
   =N\zeta^{-d^2}(-1)^u
      \zeta^{u(d-u-1)}\frac{F_uF_{d-u}}{F_d},
                  \qquad \ell=p^{-1}.
 \end{split}                                                    \tag{1}
\]
The total generators use
\(\Delta F=F\otimes I+K^{-1}\otimes F\),
\(\Delta\mathcal E=\mathcal E\otimes K+I\otimes\mathcal E\),
and \(\Delta K=K\otimes K\). A Hopf intertwiner means a map commuting
with these total generators (or the corresponding generators on its
specified input and output objects).
An index outside \(0,\ldots,d\) gives zero. Write
\(\bar u=d-u\). All nonzero cup entries and their inverses are
holomorphic units near \(t=0\), since their factorial indices are less
than \(N\). Directly from (1),
\[
 p_{\bar u}=(-1)^dK_u^{-1}p_u,
 \qquad \ell_{u,\bar u}=\frac1{p_{\bar u}}
                         =\frac{(-1)^dK_u}{p_u}.
                                                               \tag{2}
\]
Thus the literal ordinary closing convention is
\[
               \ell p^T=p\ell^T=(-1)^dK.                       \tag{3}
\]
The opposite snake is \(\ell^Tp=(-1)^dK^{-1}\); it must not
be substituted for (3). For two physical heads the signs cancel.
Put
\[
       P=K\otimes K,\qquad
       \operatorname{tr}_q Z=\operatorname{Tr}(PZ),
              \qquad S=K^{-2}\otimes I.                         \tag{4}
\]

Fix all original matching labels except the label of the block under
consideration. Keep its original cyclic orders, outside bends and exposed
physical mark. As in the marked four-port theorem, first replace that
marked scalar by the retained first normal of its ordinary closure.
The ordinary exterior is a holomorphic functional \(C_t\) on
arbitrary matrices in the two-head slot.

Cut this ordinary exterior at that slot, with its two ordered heads
still oriented as in (1). It gives a regular Hopf intertwiner
\(Y_t:V\otimes V\longrightarrow V\otimes V\). All outside
coupons, crossings, reversals and bends are included in this cut
operator. The two literal closings give, on **every** matrix array \(Z\),
\[
 C_t(Z)=\operatorname{tr}_q(Y_tZ)
      =\sum_{a,b,u,v}K_aK_b
                  (Y_t)_{ab;uv}Z_{uv;ab}.                     \tag{5}
\]
This is an ordinary index contraction, not an identity asserted only
on intertwiners. Equivalently its entries are fixed by
\[
        (Y_t)_{ab;uv}=(K_aK_b)^{-1}C_t(E_{uv;ab}),              \tag{6}
\]
where \(E_{uv;ab}\) has its single nonzero entry at the indicated
output and input. In (5), each closed physical line contributes its
factor \((-1)^dK\) from (3). Cutting the same diagram proves
Hopf covariance of \(Y_t\), since all remaining coupons and the
cup/cap dualities are genuine intertwiners. No physical marked row
is moved through a cup in this construction: \(C_t\) is the ordinary
exterior obtained after the whole-network trace-normal identity.

## 2. The exact transpose of the pivotal turn

Use precisely the bend and cyclic turn of the completed block:
\[
 \begin{split}
 B(X)_{abce}
     &=\sum_{u,v}X_{ab;uv}p_{ue}p_{vc},\\
 (R\Psi)_{abce}&=(-1)^dK_a\Psi_{bcea},
                    \qquad A=B^{-1}RB.
 \end{split}                                                    \tag{7}
\]
They are holomorphic near the root. The turn preserves invariant
four-tensors, so \(A\) takes Hopf intertwiners to Hopf intertwiners.
There is a useful entry formula valid without that restriction:
\[
              A(X)_{ab;uv}
                 =\frac{p_a}{p_v}X_{b,\bar v;\bar a,u}.
                                                               \tag{8}
\]
Indeed \(B(X)_{abce}=X_{ab;\bar e,\bar c}p_{\bar e}p_{\bar c}\),
and
\(B^{-1}(\Psi)_{ab;uv}=\Psi_{ab,\bar v,\bar u}/(p_up_v)\).
Substitute \(R\) and then use (2).

For arbitrary matrices \(X,Y\), the literal transpose identity is
\[
 \boxed{\quad
 \operatorname{tr}_q\bigl(Y A(X)\bigr)
       =\operatorname{tr}_q\bigl(S A(Y)X\bigr).
 \quad}                                                        \tag{9}
\]
To check every clock and ordering, expand the left side with (8),
and reindex its coefficient of \(X_{kl;ij}\). That coefficient is
\[
 K_jK_l^{-1}\frac{p_{\bar i}}{p_{\bar l}}
                       Y_{j,\bar l;\bar i,k}
  =K_i^{-1}K_j\frac{p_i}{p_l}
                       Y_{j,\bar l;\bar i,k},                  \tag{10}
\]
which is exactly the coefficient on the right of (9).

The clock \(S\) cannot be deleted on all arrays. For example
\(A(I)=|p\rangle\langle\ell|\), where the cup and cap are
flattened into a vector and row. Taking \(Y=I\) in (9) gives the
all-array density
\(S|p\rangle\langle\ell|\). Its image is spanned by
\((K^{-2}\otimes I)p\), which is generally not invariant.
Consequently a purported all-array transpose with a Hopf density
would be false.

## 3. The clock cancels on an entire Hopf family

For a Hopf intertwiner \(Z\) on \(V\otimes V\), define
\[
             U=\operatorname{Tr}_2((I\otimes K)Z).
                                                               \tag{11}
\]
It is a scalar operator on \(V\). Here is the convention check
without dividing by a quantum dimension. The ordinary partial
cup/cap closing of the second head has entries
\[
 \sum_{i,j,k}Z_{ai;cj}p_{jk}\ell_{ik}
       =(-1)^d\sum_iK_i Z_{ai;ci}
       =(-1)^dU_{ac},                                         \tag{12}
\]
by \(p\ell^T=(-1)^dK\). This closing is an intertwiner. At
generic \(\zeta\), the distinct \(K\)-weights make its matrix
diagonal, and the nonzero interior \(F\)-arrows force its adjacent
diagonal entries to agree. Hence \(U=zI\). The scalar \(z\) is
one matrix entry, holomorphic when \(Z\) is holomorphic. No division
by \([N]_{\zeta}\), which vanishes at the root, has occurred.

Since \(\operatorname{Tr}K^{-1}=\operatorname{Tr}K\), (11) gives
\[
 \operatorname{tr}_q(SZ)
       =z\operatorname{Tr}K^{-1}
       =z\operatorname{Tr}K
       =\operatorname{tr}_q Z.                               \tag{13}
\]
For Hopf intertwiners \(X,Y\), their product \(A(Y)X\) is again
Hopf. Equations (9) and (13) prove the restricted reciprocity
\[
 \boxed{\quad C_t(A_tX_t)
       =\operatorname{tr}_q(\widetilde Y_tX_t),
                   \qquad \widetilde Y_t=A_t(Y_t),\quad}       \tag{14}
\]
for every holomorphic Hopf family \(X_t\). The replacement exterior
\(\widetilde Y_t\) is regular and Hopf. Thus (14) may be
differentiated as a **whole family**. It does not assert equality
of the two extensions on arbitrary \(X_t'\).

For comparison, on the right-hand extension in (14), an analytic
cluster projector \(Q_t\) satisfies
\[
           \operatorname{tr}_q(\widetilde Y_tQ_t')=0.           \tag{15}
\]
Differentiate \(Q_t^2=Q_t\): its derivative has only off-diagonal
blocks relative to \(Q_t\). Both \(P\) and \(\widetilde Y_t\)
commute with \(Q_t\), so their trace against those blocks is zero.
The original literal quantity \(C_t(A_tQ_t')\) need not be zero.
Its compensating exterior and turn derivatives are retained by the
total identity (14).

## 4. Root values and Hermite coefficients of the exterior

The actual generic pair Casimir
\(\Omega_t=F_{\rm tot}\mathcal E_{\rm tot}
                +\zeta K_{\rm tot}+\zeta^{-1}K_{\rm tot}^{-1}\)
has eigenvalues
\[
       \lambda_g(t)=\zeta^{2g+1}+\zeta^{-2g-1},
                         0\le g\le d.                         \tag{16}
\]
Its generic projectors are \(\Pi_g(t)\). The tensor product is
multiplicity-free, with summand of highest weight \(2g\), so write
\(\widetilde Y_t\Pi_g=y_g(t)\Pi_g\).

Each \(y_g\) is holomorphic at the root. An explicit way to see
this, without a possibly singular spectral projection, uses the
highest vector in physical degree \(d-g\):
\[
 h_g(u)=(-1)^u\zeta^{u(d-2g-u-1)}
             \frac{F_{g+u}F_{d-u}}{F_gF_d},
                   \qquad 0\le u\le d-g.                       \tag{17}
\]
Its first coefficient is one. All indices are at most \(d\), so
it is holomorphic. The ratio of consecutive entries is
\(-\zeta^{d-2g-2u-2}(1-Q^{g+u+1})/(1-Q^{d-u})\),
which is precisely the two-term highest-vector equation for
\(\Delta\mathcal E=\mathcal E\otimes K+I\otimes\mathcal E\).
Consequently \(y_g\) is the first coefficient of
\(\widetilde Y_th_g\), and is holomorphic.

For a paired target let \(g'=d-g>g\), and put
\[
 \delta_g=\lambda_g-\lambda_{g'},\quad
 Q_g=\Pi_g+\Pi_{g'},\quad
 M_g=(\Omega-\lambda_{g'}I)Q_g=\delta_g\Pi_g.                 \tag{18}
\]
These are the target conventions of the completed block. Both
operators are holomorphic; \(Q_g(0)^2=Q_g(0)\) and
\(M_g(0)^2=0\). The latter is nonzero. Indeed, in the physical
degree-\(d\) block its extreme entry is
\[
 (M_g)_{d,0}
   =\frac{\zeta^{-Nd}F_d^2}
       {\prod_{h\ne g,g'}(\lambda_g-\lambda_h)},               \tag{19}
\]
by the original extreme adjugate formula. Its numerator and denominator
are root units.

The exterior divided difference
\[
          z_g(t)=\frac{y_g(t)-y_{g'}(t)}{\delta_g(t)}           \tag{20}
\]
is holomorphic. At generic \(t\),
\[
        \widetilde Y_tQ_g=y_{g'}Q_g+z_gM_g.                    \tag{21}
\]
The left side and the first term are holomorphic; the nonzero entry
(19) makes \(z_g\) holomorphic. In particular the two root values
coincide. We use the abbreviations \(y_g=y_{g'}(0)\) and
\(z_g=z_g(0)\). They are determined entirely by
\(\widetilde Y_0Q_g(0)=y_gQ_g(0)+z_gM_g(0)\).
Thus \(z_g\) retains the exterior's root nilpotent response; it is
not discarded as a moving-frame artifact.

## 5. The exact scalar first normal

Use \(\alpha\) for the original folded label of the exceptional
matching edge, to distinguish it from the target \(g\). In the
completed block,
\[
 E_\alpha(t)=\sum_{g<d-g}
       \bigl(F_{\alpha,g'}(t)Q_g(t)
                           +H_{\alpha g}(t)M_g(t)\bigr)
       +\text{the odd-level simple term},                     \tag{22}
\]
where
\[
 F_{\alpha g}(0)=F_{\alpha,g'}(0)=R_N(\alpha,g)>0,
 \qquad H_{\alpha g}
          =\frac{F_{\alpha g}-F_{\alpha,g'}}{\delta_g}.         \tag{23}
\]
All these operators and scalars are regular. At generic \(t\),
(14) and multiplicity-free decomposition give the exact scalarization
\[
 C_t(A_tE_\alpha(t))
       =\sum_{g=0}^d[2g+1]_{\zeta}
                              y_g(t)F_{\alpha g}(t).           \tag{24}
\]
The quantum dimension is \([2g+1]_{\zeta}\), with no sign, since
every generic target has even highest weight \(2g\).

For a pair put \(a_g=2g+1\), \(D_g=[a_g]_{\zeta}\),
\(D_{g'}=[2N-a_g]_{\zeta}\), and
\(\Delta_g=q^{a_g}-q^{-a_g}\). Its contribution to (24) is
\[
 \begin{split}
 D_gy_gF_{\alpha g}+D_{g'}y_{g'}F_{\alpha,g'}
  ={}&(D_g+D_{g'})y_{g'}F_{\alpha,g'}\\
   &+\delta_gD_g
       (z_gF_{\alpha,g'}+y_{g'}H_{\alpha g}
                                      +\delta_gz_gH_{\alpha g}).
 \end{split}                                                   \tag{25}
\]
All functions in (25) are evaluated at the same \(t\). Both
\(D_g+D_{g'}\) and \(\delta_g\) vanish at \(t=0\).
The original trace-normal constant is
\[
             \nu_N=\frac{2N(-1)^N}{q-q^{-1}}.
\]
Direct differentiation, with exactly the target gap of (18), yields
\[
 \frac{(D_g+D_{g'})'(0)}{\nu_N}
                      =(-1)^N(q^{a_g}+q^{-a_g}),\qquad
 \frac{\delta_g'(0)D_g(0)}{\nu_N}=(-1)^N\Delta_g^2.            \tag{26}
\]
Here \(\delta_g'(0)=2N\Delta_g\), rather than its negative.
Therefore the pair's normalized first normal is
\[
 \boxed{\quad
 \mathcal T_{\alpha g}=(-1)^N\left[
   (q^{a_g}+q^{-a_g})y_gR_N(\alpha,g)
      +\Delta_g^2\{z_gR_N(\alpha,g)
                                      +y_gH_{\alpha g}(0)\}\right].
 \quad}                                                        \tag{27}
\]
When \(N\) is odd, the simple target \(m=d/2\) has dimension
\([N]_{\zeta}\). Its normalized first normal is
\[
                 \mathcal T_{\alpha m}
                         =y_m(0)R_N(\alpha,m),                 \tag{28}
\]
since \([N]'(0)=\nu_N\) in this parity.

Finally retain the original completed source formula
\[
 h^0_\alpha\omega_\alpha^\epsilon Z_\Delta
   =\frac{k_\alpha N\omega_\alpha^\epsilon}{\nu_N}
        [t^1]\{u_\alpha(t)v_N(t)
                              C_t(A_tE_\alpha(t))\},           \tag{29}
\]
with its original scalar units \(u_\alpha(0)=v_N(0)=1\).
Here
\(h^0_\alpha=k_\alpha N s_{2\alpha}/s_\alpha^2\),
\(s_j=\prod_{r=1}^j2\sin(\pi r/N)\), \(s_0=1\), and
\(\omega_\alpha=q^{d^2/2}(-1)^\alpha q^{\alpha(\alpha+1)}\).
The exponent \(\epsilon\) is the original retained half twist.
Every pair in (25), and the simple term, vanishes at the root.
Their common scalar-unit derivatives therefore make no contribution.
The actual signed marked sector is exactly
\[
 \boxed{\quad
 h^0_\alpha\omega_\alpha^\epsilon Z_\Delta
       =k_\alpha N\omega_\alpha^\epsilon
          \left(\sum_{g<d-g}\mathcal T_{\alpha g}
              +\mathbf1_{N\ {\rm odd}}\mathcal T_{\alpha m}\right).
 \quad}                                                        \tag{30}
\]
Here \(k_\alpha=2\) on a paired original label and \(1\) at its
odd simple endpoint. The same original physical mark, its normal
constant, its half-twist phase and all original outside labels remain.
No new source normalization is used.

## 6. What has canceled and what still has to be estimated

Formula (30) contains no independent norm of \(Q_g'\), \(M_g'\),
or the moving spectral frame. Common first jets of the exterior
eigenvalue and scalar weight also cancel in (25). The exterior
information that remains is exactly its root Casimir value \(y_g\)
and root nilpotent coefficient \(z_g\). The latter can encode a
difference of moving eigenvalue derivatives; it has not been set to
zero. The scalar source coefficient \(H_{\alpha g}(0)\) likewise
retains its prescribed divided difference.

There is no universal annihilation of primitive normal channels by
the original mark. For the unrotated literal ordinary two-head trace,
\[
 \frac1{\nu_N}[t]\operatorname{tr}_qQ_g
        =(-1)^N(q^{a_g}+q^{-a_g}),\qquad
 \frac1{\nu_N}[t]\operatorname{tr}_qM_g
        =(-1)^N\Delta_g^2.                                    \tag{31}
\]
The second number is nonzero for every paired target, and has absolute
value \(4\sin^2(\pi a_g/N)\ge16/N^2\). This is a local trace
identity, not a knot volume example. In the rotated matching problem
the relevant exterior is \(\widetilde Y=A(Y)\); it may change or
annihilate these scalar responses.

Thus (30) removes the need to estimate large matrix projectors and
their generic derivatives separately. It does not bound \(y_g,z_g\),
choose a geometric contour, or prevent cancellation between the terms
of (30). In particular it does not prove that a classical geometric
critical equation annihilates the source-visible residual of a quantum
trial packet. A sharp scalar exterior estimate with the original
phases remains necessary for that application.

## Complete direct sources

All four complete matching texts were read. The first fixes the literal
physical pivotal orientation; the second supplies the ordinary exterior
and unchanged marked normal; the third supplies the exact completed
operator, bend and scalar units; the fourth supplies the regular generic
Hopf network and the original whole-network mark. The transpose identity,
partial-trace reciprocity and scalar Hermite reduction are proved above.

| Source | SHA-256 |
|---|---|
| [All-channel marked contraction](actual_trivalent_all_channel_marked_contraction.md) | d9515c57979304914d6cbd00701d3f465b736a223494705f6fff884fdfce157d |
| [Original matching-edge block](actual_matching_edge_marked_four_port_block.md) | 79ae5dc22fb99d1154a6060423f5a762f93887a784d374e885439bb9893b242a |
| [Completed projector pairs](actual_matching_edge_completed_projector_block.md) | c56b271e7b336e6b16b2f5ef6c63abf409b231fb1665a4c71a58b31494f95acc |
| [Full original matching-graph source](general_matching_graph_full_normal_source.md) | aba957dba520a7d5cb3373d5bbd42bc6766a92cb80e18cc4823007e6bd7ef1bd |

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical experiment, build, git operation,
previous-final edit or public-document change was performed.
