# Exact twist observations, a positive metric, and its blind directions

Research deduction, 6 November 2026. All operators and observations
below belong to the original full Newton algebra. No source evaluation,
root computation, numerical certificate, or manuscript change is used.

There is an exact positive observation norm at odd prime levels in
which every fixed crossing power has bounded distortion, independently
of the level. Its ungrouped physical-jet version is positive at every
integer level, with the same fixed-twist bound. Recovering the
observation norm uses a window of \(4N\) different closing twists.
A physical turn has exponential distortion in this norm on already
proved original sources. Moreover, a fixed finite window cannot be
coercive on the whole algebra, and at infinitely many composite levels
even all integer twist observations miss a nonzero first-normal
direction. These assertions distinguish a useful positive average
from a lower bound for one fixed filled source.

## 1. The literal twist-and-turn observation

Put \(D=N-1\), \(q=e^{\pi i/N}\), \(\eta=(-1)^D\), and
\(\kappa=q^{D^2/2}\). Use the canonical original algebra
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\), its normalized Newton
basis, crossing \(M\), turn \(J\), and trace \(\phi_N\). For a
coefficient column \(f\),
\[
 z_n(f)=\phi_N(R^n f)=\mathbf e_D^T M^n f
                    =\mathbf e_0^T A_n f,
 \qquad A_n=JM^n,\qquad n\in\mathbb Z.
 \tag{1}
\]
Thus \(z_n\) is the actual turned-cap observation after the arbitrary
signed twist-and-turn \(A_n\). It is not a trace of the operator
matrix. Powers, scalar phases, and the first normals are unchanged.

Index the distinct double physical nodes by
\[
 0\le j<\lfloor N/2\rfloor,\quad
 \theta_j=(2j+1)\pi/N,\quad c_j=2\cos\theta_j,
 \quad d_j=4-c_j^2=4\sin^2\theta_j.
 \tag{2}
\]
At odd levels there is also the simple node \(c_*=-2\). The exact
[full Hermite trace](research_physical_normal_lift.md), equation (14),
and the [original crossing jets](research_arbitrary_power_source_compilation.md),
equation (21), give
\[
 \begin{split}
 \phi_N(f)&=\eta\sum_j\{d_j f'(c_j)-c_j f(c_j)\}
                   +\mathbf1_{N\text{ odd}}f(-2),\\
 \lambda_j:=R(c_j)&=\kappa(-1)^j q^{j+j^2},\qquad
 \alpha_j:=\frac{R'(c_j)}{R(c_j)}
            =\frac{i(D-2j)}{4\sin\theta_j}.
 \end{split}
 \tag{3}
\]
The corresponding eigenvalue at the odd simple node is obtained by
putting \(j=D/2\) in the value formula. All these eigenvalues have
modulus one. Set
\[
 a_j=\eta\{d_j f'(c_j)-c_j f(c_j)\},\qquad
 b_j=\eta i(D-2j)\sin\theta_j f(c_j),\qquad
 a_*=f(-2),\quad b_*=0.
 \tag{4}
\]
The starred pair is present only at odd levels. Equations (3) retain
the derivative of \(R^n\), and therefore imply, for every integer \(n\),
\[
              z_n(f)=\sum_j\lambda_j^n(a_j+n b_j)
                 +\mathbf1_{N\text{ odd}}\lambda_*^n a_*.
 \tag{5}
\]
In particular the normal contribution is linear in the twist power;
it cannot be dropped when forming a positive average.

## 2. An exact two-block Fourier reconstruction

Let \(L=2N\), \(\zeta_j=\lambda_j/\kappa\), and
\(y_n=\kappa^{-n}z_n\). Every \(\zeta_j\) is an \(L\)-th root
of unity. Group coincident \(\zeta_j\)'s, including the simple node,
and write \(A_\zeta=\sum_{j:\zeta_j=\zeta}a_j\) and
\(B_\zeta=\sum_{j:\zeta_j=\zeta}b_j\). For \(0\le n<L\), define
\[
 v_n=\frac{y_{n+L}-y_n}{L},\qquad w_n=y_n-nv_n.
 \tag{6}
\]
The exact identities are
\[
 \begin{split}
 v_n&=\sum_\zeta B_\zeta\zeta^n,&
 w_n&=\sum_\zeta A_\zeta\zeta^n,\\
 B_\zeta&=\frac1L\sum_{n=0}^{L-1}v_n\zeta^{-n},&
 A_\zeta&=\frac1L\sum_{n=0}^{L-1}w_n\zeta^{-n}.
 \end{split}
 \tag{7}
\]
They follow directly from (5), then ordinary finite Fourier
orthogonality. Consequently the positive form
\[
 \mathcal E_N(f):=\frac1L\sum_{n=0}^{L-1}
                  (|v_n|^2+|w_n|^2)
                =\sum_\zeta(|A_\zeta|^2+|B_\zeta|^2)
 \tag{8}
\]
has precisely the common kernel of all observations \(z_n\),
\(n\in\mathbb Z\). The first \(4N\) observations already determine
every observation at every signed twist power.

This average has only polynomial cost relative to the raw window.
Indeed \(w_n=(1+n/L)y_n-(n/L)y_{n+L}\), so Cauchy--Schwarz gives
\[
 \mathcal E_N(f)\le\frac6L\sum_{n=0}^{2L-1}|z_n(f)|^2,
 \qquad
 \frac1L\sum_{n=0}^{2L-1}|z_n(f)|^2
                         \le10L^2\mathcal E_N(f).
 \tag{9}
\]
For the second estimate use \(y_n=w_n+nv_n\) and
\(y_{n+L}=w_n+(n+L)v_n\), with \(0\le n<L\). The constants
in (9) are deliberately generous and valid for \(N\ge2\).

### Keeping one original carrier parity

An original fixed carrier allows powers of just one parity. Fix
\(\epsilon\in\{0,1\}\), and use only
\(n=\epsilon+2r\). Define
\[
 Z_r=\kappa^{-\epsilon-2r}z_{\epsilon+2r},\quad
 \tau_j=\zeta_j^2,\quad
 a_j^{(\epsilon)}=\zeta_j^\epsilon(a_j+\epsilon b_j),\quad
 b_j^{(\epsilon)}=2\zeta_j^\epsilon b_j.
 \tag{9a}
\]
Then \(Z_r=\sum_j(a_j^{(\epsilon)}+r b_j^{(\epsilon)})\tau_j^r\),
with the simple-node convention unchanged. All \(\tau_j\) are
\(N\)-th roots of unity. Use (6)--(8) with \(L=N\), \(Z\) in
place of \(y\), and these new coefficient pairs, grouping equal
\(\tau\)'s. This reconstructs every observation in that parity
from the \(2N\) powers
\(\epsilon,\epsilon+2,\ldots,\epsilon+2(2N-1)\).

At odd prime levels equality of two \(\tau_j\)'s again implies
\((j-k)(j+k+1)=0\pmod N\), so this parity-specific positive form,
denoted \(\mathcal E_N^{(\epsilon)}\), is faithful. Its local
change from (8) is a unit scalar times
\((a,b)\mapsto(a+\epsilon b,2b)\). The norms of this change and
its inverse are at most \(3\) and \(2\), respectively. Thus
\[
       \tfrac14\mathcal E_N(f)
       \le\mathcal E_N^{(\epsilon)}(f)\le9\mathcal E_N(f)
                       \qquad(N\text{ odd prime}).
 \tag{9b}
\]
The raw-window comparison (9) applies with \(L=N\). In particular
all the ensuing polynomial-coercivity conclusions have a version
using only powers allowed by the original carrier. The chosen
window still grows with \(N\); no fixed filling has been changed
in an asymptotic assertion.

## 3. All-level positive norm and prime-level observation coercivity

At every odd prime \(N\), the eigenvalues in (3) are distinct at the
distinct physical nodes. Indeed equality implies
\((j-k)(j+k+1)=0\pmod N\), so \(j=k\) or \(j+k=N-1\).
The latter is exactly the two representatives of one double node.
This is also the eigenvalue calculation in
[the trace-completion note](research_mixed_trace_completion_and_observation.md),
Section 4. Thus (8) is a positive definite norm squared on the entire
original \(N\)-dimensional algebra at these levels.

For an explicit comparison, put
\[
 \|f\|_{\rm jet}^2=\sum_j\bigl(|f(c_j)|^2+|f'(c_j)|^2\bigr)
                         +\mathbf1_{N\text{ odd}}|f(-2)|^2.
 \tag{10}
\]
At every integer level \(N\ge2\), retain the coefficient pairs before
grouping equal eigenvalues:
\[
 \widetilde{\mathcal E}_N(f)
     =\sum_j(|a_j|^2+|b_j|^2)
                       +\mathbf1_{N\text{ odd}}|a_*|^2.
 \tag{10a}
\]
Each double-node map \((f(c_j),f'(c_j))\mapsto(a_j,b_j)\) in (4)
is invertible, and the simple-node map is the identity. Full Hermite
interpolation therefore makes (10a) positive definite at every level.
It equals the observation form \(\mathcal E_N\) at odd primes.
At levels with eigenvalue collisions these forms differ: (10a)
retains individual jets, whereas (8) sees only their grouped sums.

Every double-node sine is at least \(2/N\), and \(D-2j\ge1\).
Hence \(d_j\ge16/N^2\) and
\(2/N\le(D-2j)\sin\theta_j\le N\). Equations (4) give
\[
 |f(c_j)|\le\frac N2|b_j|,\qquad
 |f'(c_j)|\le\frac{N^2}{16}|a_j|+
                              \frac{N^3}{16}|b_j|.
\]
The reverse estimates use \(d_j\le4\) and \(|c_j|\le2\).
After summing, at every integer level one obtains
\[
 N^{-6}\|f\|_{\rm jet}^2\le\widetilde{\mathcal E}_N(f)
                              \le8N^2\|f\|_{\rm jet}^2.
 \tag{10b}
\]
In particular at odd prime levels the observation form satisfies
\[
          N^{-6}\|f\|_{\rm jet}^2
               \le\mathcal E_N(f)\le8N^2\|f\|_{\rm jet}^2.
 \tag{11}
\]
The [complete Hermite norm lemma](../papers/circle-tree-volume/finite-bounds.tex)
also compares this norm polynomially with the canonical polynomial's
real interval norm. No assertion of polynomial equivalence with the
Newton coefficient Euclidean norm is needed.

There is an exact transport law, valid even when (8) is only
semidefinite. Multiplication by \(R^k\) sends
\[
 (A_\zeta,B_\zeta)\longmapsto
       (\kappa\zeta)^k(A_\zeta+kB_\zeta,B_\zeta).
 \tag{12}
\]
The simple-node block has \(B=0\). The shear and its inverse have
operator norm at most \(1+|k|\). Before grouping, the identical
calculation sends \((a_j,b_j)\) to
\(\lambda_j^k(a_j+kb_j,b_j)\), so at every integer level
\[
 \frac{\widetilde{\mathcal E}_N(f)^{1/2}}{1+|k|}
 \le\widetilde{\mathcal E}_N(R^k f)^{1/2}
 \le(1+|k|)\widetilde{\mathcal E}_N(f)^{1/2}.
 \tag{12a}
\]
For the grouped observation form it gives
\[
 \frac{\mathcal E_N(f)^{1/2}}{1+|k|}
 \le\mathcal E_N(R^k f)^{1/2}
 \le(1+|k|)\mathcal E_N(f)^{1/2}.
 \tag{13}
\]
This is a level-independent distortion bound for each fixed signed
twist. It does not make its nontrivial unit-circle Jordan blocks
unitary, and is consistent with the earlier exact unitarization
obstructions.

Combining (9) and (11), at prime levels at least one power in the
window \(0\le n<4N\) obeys
\[
                    |z_n(f)|\ge
                    \frac{\|f\|_{\rm jet}}{\sqrt{12}\,N^3}.
 \tag{14}
\]
The maximizing power is allowed to depend on both \(f\) and \(N\).
Equation (14) is not a lower bound for a specified fixed filling.
For one prescribed carrier parity, (9b) gives the same conclusion
among its \(2N\) displayed powers with denominator
\(\sqrt{48}\,N^3\) instead. The fixed-window nullspace argument
below applies equally to any finite set in that parity, and the
composite example is invisible to both parities simultaneously.

## 4. A fixed window and all composite-level twists can be blind

First fix any \(r\) integer powers, independently of \(N\). The
radical of the original algebra consists of polynomials whose
physical values vanish, retaining the independent first normals.
Its dimension is \(\lfloor N/2\rfloor\). If this exceeds \(r\),
the \(r\) scalar observations have a nonzero common kernel even on
the radical. Thus no strictly positive full-space coercivity constant,
polynomial or otherwise, exists for any such fixed finite window.

For a consecutive window this failure has a useful exact form.
Fix a starting power \(q_0\in\mathbb Z\), and choose an odd prime
\(N\ge2r+3\). Take \(r+1\) distinct double nodes, with distinct
\(\zeta_0,\ldots,\zeta_r\). Prescribe zero physical values and
zero other normals, and set
\[
 a_j=\frac{\zeta_j^{-q_0}}
              {\prod_{k\ne j}(\zeta_j-\zeta_k)},\qquad
 f'(c_j)=\frac{\eta a_j}{d_j},\quad 0\le j\le r.
 \tag{15}
\]
Full Hermite interpolation gives a unique nonzero canonical original
polynomial. The elementary leading-coefficient identity for Lagrange
interpolation gives
\[
 z_{q_0}(f)=\cdots=z_{q_0+r-1}(f)=0,
                  \qquad z_{q_0+r}(f)=\kappa^{q_0+r}.
 \tag{16}
\]
No limiting or approximate cancellation is involved.

There is a stronger obstruction at infinitely many composite levels.
Take \(N=49h\), with \(h\ge1\) odd, and the two double-node indices
\[
                  j=\frac{7h-1}{2},\qquad
                  k=\frac{35h-1}{2}.
 \tag{17}
\]
They lie strictly below \((N-1)/2\), and their physical colors are
\(2\cos(\pi/7)\) and \(2\cos(5\pi/7)\), respectively.
Yet their eigenvalues agree, since
\[
 (j-k)(N+j+k+1)=-980h^2\in2N\mathbb Z.
 \tag{18}
\]
Prescribe zero physical values, \(f'(c_j)=1/d_j\),
\(f'(c_k)=-1/d_k\), and all other normals zero. This nonzero
radical polynomial satisfies
\[
                         z_n(f)=0\quad\hbox{for every }n\in\mathbb Z.
 \tag{19}
\]
Thus increasing the number of scalar twist observations without
changing the observation cannot give a positive definite metric at
these levels. In general a coincident-eigenvalue group with \(r_d\)
double nodes and \(r_s\in\{0,1\}\) simple nodes has an invisible
space of dimension \(2r_d+r_s-2\) when \(r_d>0\); a lone simple
group has none. Only the two sums \(A_\zeta,B_\zeta\) survive.

The polynomials in (15) and (19) are valid inputs in the full original
algebra. They are not asserted to arise from one fixed hyperbolic
short-filled tangle as \(N\) varies. They disprove universal algebraic
coercivity from the stated observations; they do not disprove the
volume conjecture or a source-specific overlap theorem.

## 5. The physical turn has exponential cost in the positive metric

The twist bound (13) cannot be extended to the whole \(A_k=JM^k\)
with polynomial distortion in this same metric. Fix a signed power
\(|p|\ge2\), and use the actual terminal source
\[
                  H_{p,N}=J R^p.
 \tag{20}
\]
The [whole terminal theorem](research_uniform_terminal_family_and_star_fillings.md)
gives its nonzero complete packet
\(|H_{p,N}(-2)|=\exp(NM_p+O_p(\log N))\), with \(M_p>0\).
Its whole real-boundary estimate and the complete Hermite norm lemma
also give \(\|H_{p,N}\|_{\rm jet}\le N^{C_p}e^{NM_p}\).
At odd prime levels the simple-node term in (8) is exactly
\(|H_{p,N}(-2)|^2\). Thus
\[
 \mathcal E_N(H_{p,N})^{1/2}
                  =\exp(NM_p+O_p(\log N)).
 \tag{21}
\]
By contrast \(\mathcal E_N(1)^{1/2}=N^{O(1)}\), and (13) implies
\(\mathcal E_N(R^p)^{1/2}=N^{O_p(1)}\). Consequently, along
these levels, the norm of the actual turn in this positive metric
obeys
\[
 \|J\|_{\mathcal E_N}\ge e^{NM_p}N^{-C_p},\qquad
 \|J\|_{\mathcal E_N}\|J^{-1}\|_{\mathcal E_N}
                              \ge e^{2NM_p}N^{-2C_p}.
 \tag{22}
\]
The second inequality uses \(J^{-1}=J\). In the reverse direction,
the same actual source satisfies \(JH_{p,N}=R^p\), so a single turn
can lose precisely this positive exponential rate in the norm.

This sharpens, in an explicit original observation metric, the
[known failure of unrestricted packet closure under turns](research_boundary_crossing_packet_preservation.md),
Section 7. The cost is exponential in \(N\), despite the fact that
the source and the crossing power \(p\) are fixed. It is not one of
the polynomial losses that can be absorbed into a volume asymptotic.

The useful exact information is therefore (7), (12), and (13):
fixed twists transport a complete positive observation norm with
controlled cost on the faithful prime-level space, or on the
observable quotient at other levels. The ungrouped form (10a)
provides the same positive fixed-twist control on the full space
at every level, but scalar twist observations cannot recover its
invisible directions when collisions occur. To close an arbitrary fixed
short component, one still needs a quantitative estimate for its
specified turn and final row. Neither selecting an \(N\)-dependent
power from (14), nor discarding the composite-level radical in (19),
retains that original fixed filling problem.

## 6. A metric-independent exponential tradeoff

The limitation is not confined to the particular norm (8). Let
\(\mathsf H_N\) be any positive definite Hermitian metric on the
full original coefficient space, with no restriction on its
level-dependent condition number. Write \(\|\cdot\|_{\mathsf H_N}\)
for the induced operator norm. The exact original identities in
[the positive-three theorem](research_positive_three_crossing_cycle.md),
Theorem 1, give
\[
                  M(JM^3)M^{-1}=\kappa M^*M .
 \tag{23}
\]
Here the adjoint on the right is the original Euclidean adjoint,
irrespective of the newly chosen metric. In particular
\(\rho(JM^3)=\rho(M^*M)\ge N^{-1}\operatorname{Tr}(M^*M)\).
Theorem 2 of that same note, with one vertex, proves
\[
 \operatorname{Tr}(M^*M)
   =e^{2c_{\rm cyc}N}
       \left\{\frac{\sqrt{\rho_0}}{1-\rho_0}+O(N^{-1/2})\right\},
 \quad c_{\rm cyc}=2\int_0^{5/6}\log(2\sin\pi x)\,dx>0,
 \quad \rho_0=\frac{5-\sqrt{21}}2.
 \tag{24}
\]
The unit scalar \(\kappa\) has been removed only by the exact
similarity (23). Thus, for a fixed constant \(C>0\) and every
sufficiently large integer level, every such metric satisfies
\[
 \boxed{\quad
 \|J\|_{\mathsf H_N}\|M^3\|_{\mathsf H_N}
       \ge \rho(JM^3)
       \ge C N^{-1}e^{2c_{\rm cyc}N}.
 \quad}
 \tag{25}
\]
The first inequality is spectral-radius domination followed by
submultiplicativity. It needs no asymptotic information about the
eigenvectors or about the new metric.

Even the full Gaussian trace asymptotic is unnecessary for the
existence of an exponential obstruction. Take
\(j=\lfloor2N/3\rfloor\) and \(k=\lfloor N/3\rfloor\). The original
crossing entry has modulus \(S_j/(S_kS_{j-k})\), where
\(S_r=\prod_{\ell=1}^r2\sin(\pi\ell/N)\). The elementary
sine-factorial estimate gives
\[
 \log|M_{jk}|=
 N\{\mathcal J(2/3)-2\mathcal J(1/3)\}+O(\log N)
                 =Nc_{\rm cyc}+O(\log N),
 \qquad
 \mathcal J(x)=\int_0^x\log(2\sin\pi t)\,dt .
 \tag{25a}
\]
Here \(\mathcal J(1-x)=-\mathcal J(x)\) and
\(c_{\rm cyc}=-3\mathcal J(1/3)>0\), as in the cited theorem.
The direct bound
\(\rho(M^*M)\ge N^{-1}\operatorname{Tr}(M^*M)
 \ge N^{-1}|M_{jk}|^2\)
already proves the right side of (25) with a possibly larger
polynomial denominator. Formula (24) supplies its sharper displayed
prefactor.

Consequently no positive metric makes both the original turn and
the fixed triple twist subexponential. In particular it cannot make
both \(J\) and \(M\) subexponential, since
\(\|M^3\|_{\mathsf H_N}\le\|M\|_{\mathsf H_N}^3\).
At prime levels (13) gives \(\|M^3\|_{\mathcal E_N}\le4\), so
(25) strengthens its turn bound to
\(\|J\|_{\mathcal E_N}\ge(C/4)N^{-1}e^{2c_{\rm cyc}N}\).

This is an operator-norm obstruction on the full original space.
It does not preclude almost invariance, controlled transport on a
specified source direction, or a nonzero observation after a
quantitatively calibrated scalar normalization. Nor does the cyclic
rate in (24) identify the action of an arbitrary open component.
Such source-specific possibilities must retain their original
observation and exponential normalization; a universal positive
metric with only polynomial losses cannot supply them.
