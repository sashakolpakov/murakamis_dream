# Exact endpoint Euler kernels and pivotal interface matching

Private written proof, 18 November 2026.

The compressed Euler transition E and the closing-current adapter C
give an exact matching calculation on the original finite heads.
Its input is a specified transfer diagonal of the actual neighboring
network. The calculation keeps the finite Fourier projector, the
upper-collar monomial, and the outward interface row. It does not
replace a projector by a delta kernel or obtain scalar noncancellation
from an invertible crossing.

The unconditional statements are the source calibration, joint kernel,
and current decomposition below. Section 5 gives explicit conditional
profiles at the two endpoint scales. Its packet assumptions are not
asserted for a geometric source: in particular, a flat framing family
may require a correlated, rather than two independent, normal profile.

## 1. A crossing and its actual neighboring matrix

Use E's notation
\[
 d=N-1,\quad h=2\pi i/N,\quad q=e^{h/2},\quad Q=e^h,\quad
 x=-M/q,\quad \rho=q-q^{-1}.
 \tag{1}
\]
The root calculations below have \(M=1\). The finite identities also
hold on E's normal bidisk wherever their displayed denominators are
units. Write \(A=\mathcal E_1F_2\). Its positive Euler factor and its
inverse will be denoted \(\Theta^\varepsilon\), \(\varepsilon=\pm1\):
\[
 \Theta^\varepsilon
   =\sum_{n=0}^{d}\gamma_{N,n}^{\varepsilon}(A/h)^n,\qquad
 \gamma_{N,n}^{+}=\frac{(-1)^nq^{n^2}h^n}{F_n(Q)},\quad
 \gamma_{N,n}^{-}=\frac{q^nh^n}{F_n(Q)}.
 \tag{2}
\]
Here \(F_n(Q)=\prod_{j=1}^n(1-Q^j)\), \(F_0=1\). E proves
\[
 |\gamma_{N,n}^{\varepsilon}|
       \le C^n/n!,\qquad
 \left|\gamma_{N,n}^{\varepsilon}-\varepsilon^n/n!\right|
       \le C^n n^2/(Nn!).
 \tag{3}
\]
The zero endpoint arrows, Cartan diagonal, flip, and common crossing
scalar remain literal. For a negative crossing those remaining factors
occur in their inverse order.

Here is an exact way to use the donor as a pivotal head even if the
original diagram did not place its reduced cut there. Write the original
finite contraction, with all spectators included, as
\[
 \Phi=\varkappa\,\operatorname{Tr}
          (P_{\rm old}\,L\,\Theta^\varepsilon R).
\]
The original cut/pivots are in \(P_{\rm old}\); the remaining crossing
factors and every other coupon are in \(L,R\). Let
\[
 g_1=K_1^{1-N},\qquad
 \mathscr E=g_1^{-1}R P_{\rm old}L.
 \tag{4}
\]
Ordinary finite cyclicity, not a change of cut convention, gives
\[
                    \Phi=\varkappa\operatorname{Tr}
                                (g_1\mathscr E\Theta^\varepsilon).
 \tag{5}
\]
The compensating \(g_1^{-1}\) stays inside \(\mathscr E\). Thus this
formula does not insert a free pivot, average the highest cut, or assume
that an opened marked network is scalar or intertwines.

Apply E's diagonal endpoint gauges to the whole network, including
\(\mathscr E\) and every exposed row and column. They commute with
\(g_1\). The flag coupon used below is conjugated too. Let
\(E_N=\operatorname{Tr}_{\rm spectators}\mathscr E\) in this gauged
two-head basis. The actual coefficients needed here are
\[
 e_{N,n}(a,b)
       =(E_N)_{(a,b),(a-n,b+n)}.
 \tag{6}
\]
They retain the original framing, marks, Cartan factors and cut. No
positivity or phase condition on (6) is part of (5).

In either endpoint gauge the transfer is a weighted unilateral shift:
\[
 T_N=A/h,\qquad
 T_N|a,b\rangle=t_N(a,b)|a-1,b+1\rangle.
 \tag{7}
\]
At a forced zero arrow its coefficient is zero. Put
\[
 t_{N,n}(a,b)=\prod_{j=0}^{n-1}t_N(a-j,b+j),\qquad t_{N,0}=1.
 \tag{8}
\]
The product is zero if a physical endpoint is crossed.

## 2. The exact joint Fourier projector

Let \(I=[L_1,U_1]\), \(J=[L_2,U_2]\) be integer intervals and
\(P=P_I\otimes P_J\), with \(R_i=U_i-L_i\). E's monotone
compression identity gives
\[
 P T_N^nP=(PT_NP)^n
 \quad\text{on }\operatorname{im}P.
 \tag{9}
\]
Use the root Fourier matrix \(\mathcal F_{a,j}=N^{-1/2}Q^{aj}\)
on each head. For \(\mathbf j,\mathbf k\in\{0,\ldots,d\}^2\), set
\[
 t_i=Q^{k_i-j_i},\qquad \chi=Q^{j_1-j_2}.
 \]
Direct substitution of the output indices \(a-n,b+n\) proves
\[
\begin{split}
 &(\mathcal F^{*\otimes2}P\Theta^\varepsilon P
                   \mathcal F^{\otimes2})_{\mathbf j,\mathbf k}\\
 &\quad=\frac1{N^2}
  \sum_{n=0}^{\min(R_1,R_2)}
    \gamma_{N,n}^{\varepsilon}\chi^n
       \sum_{a=L_1+n}^{U_1}\sum_{b=L_2}^{U_2-n}
               t_{N,n}(a,b)t_1^a t_2^b .
\end{split}                                                    \tag{10}
\]
This is a transfer-diagonal kernel, not a product of two asymptotic
evaluation maps. In the summation domain the unweighted monomial
factor is exactly
\[
 t_1^{L_1+n}K_{R_1-n}(t_1)\,
 t_2^{L_2}K_{R_2-n}(t_2),\qquad
 K_R(t)=\sum_{a=0}^R t^a,\quad K_R(1)=R+1.
 \tag{11}
\]
The weights (8) remain inside (10). In particular an upper recipient
collar retains \(t_2^{d-R_2}\). Neither endpoint is dropped. Off the
root, keep this root Fourier matrix fixed and differentiate the actual
finite coefficients; changing the Fourier basis is not required.

The source decomposition is also exact. On the full two-head space,
\[
\begin{split}
 \operatorname{Tr}(g_1E_N\Theta^\varepsilon P)
 ={}&\operatorname{Tr}(g_1P E_NP\Theta^\varepsilon P)\\
 &+\operatorname{Tr}(g_1P E_N(1-P)\Theta^\varepsilon P).
\end{split}                                                    \tag{12}
\]
The second term is an outgoing transfer paired with the actual
environment. Together with
\(\operatorname{Tr}(g_1E_N\Theta^\varepsilon(1-P))\), it retains the
whole source (5). It is not estimated by compressed invertibility.

There are two invariant choices useful for the endpoint calculation:
\[
 \begin{array}{c|c|c}
 \text{gauges}&I&J\\ \hline
 G_F\otimes1 &[0,R_1]&[0,d]\\
 G_F\otimes G_E &[0,R_1]&[d-R_2,d].
 \end{array}                                                   \tag{13}
\]
The transfer decreases the donor occupation. In the second line it
also decreases the recipient's distance from its upper endpoint.
Both rectangles are therefore invariant, so
\((1-P)\Theta^\varepsilon P=0\) exactly. In that case the first
term of (12), with (10), is the entire selected-input piece.
Incoming transfers from \(1-P\), and the whole complementary source,
are still present. Other collar orientations have only (9), not this
invariance.

## 3. Exact interface matching for the original pivotal current

Fix a recipient interval \(J\). For
\(W_J=E_N\Theta^\varepsilon P_J\), let \(C_a^J\) be its partial-trace
diagonal on the donor. It is explicitly
\[
 C_a^J=
 \sum_{b\in J}\ \sum_{n=0}^{\min(a,d-b)}
       e_{N,n}(a,b)\gamma_{N,n}^{\varepsilon}t_{N,n}(a,b).
 \tag{14}
\]
For the second invariant rectangle of (13), \(b+n\) automatically
stays in \(J\). Formula (14) has no untruncated transfer sum.
The selected period for \(I=[0,R]\) is
\[
              \Phi_{I,J}
        =\varkappa g_0\sum_{a=0}^R Q^{-a}C_a^J,\qquad
                     g_0=x^{1-N},
 \tag{15}
\]
at the root, because \(g_a=g_0Q^{-a}\).

Let \(Q_{\rm f}=-q^{-1}L\) be C's literal lowering coupon,
\(L|a\rangle=|a-1\rangle\), \(L|0\rangle=0\). Conjugate it with
the chosen donor gauge. The diagonal coefficient of
\(F[W_J,Q_{\rm f}]\), paired with \(g_1\), is unchanged by that
conjugation. For \(1\le a<N\) it is
\[
 h_a^{\rm phys}(C_a^J-C_{a-1}^J),\qquad
 h_a^{\rm phys}=q^{-1}g_0(Q^{-a}-1).
 \tag{16}
\]
Indeed before conjugation the coefficient of the commutator is
\(q^{-1}(C_a^J-C_{a-1}^J)\), and the returning \(F\)-arrow is
\(1-Q^a\). Multiplication by \(g_a\) gives (16).
This argument uses only diagonal entries of the partial trace, even
if the remaining marked matrix is not diagonal.

Define the localized row sum, excluding its outward interface, by
\[
             J_{I,J}^{\rm loc}
       =\varkappa\sum_{a=1}^R
                       h_a^{\rm phys}(C_a^J-C_{a-1}^J).
 \tag{17}
\]
Write \(S_{R+1}=\sum_{a=0}^R Q^{-a}\). Finite summation by parts gives
\[
 \boxed{\quad
 \frac Q\rho J_{I,J}^{\rm loc}
   =\varkappa g_0
        \left(\sum_{a=0}^R Q^{-a}C_a^J-S_{R+1}C_R^J\right).
 \quad}                                                       \tag{18}
\]
One direct check is
\[
 h_a^{\rm phys}-h_{a+1}^{\rm phys}
              =(\rho/Q)g_0Q^{-a},\qquad
 (Q/\rho)h_{R+1}^{\rm phys}=-g_0S_{R+1}.
 \tag{19}
\]
The same identity at \(a=0\), with \(h_0^{\rm phys}=0\), pays
the lower endpoint.

The full current of the projected word \(W_JP_I\) has one further
row, at \(a=R+1\), when \(R<d\):
\[
                 J_{I,J}^{\rm out}
                =-\varkappa h_{R+1}^{\rm phys}C_R^J.
 \tag{20}
\]
Thus its normalized contribution is the positive term
\(+\varkappa g_0 S_{R+1}C_R^J\), and
\[
       \frac Q\rho(J_{I,J}^{\rm loc}+J_{I,J}^{\rm out})
                            =\Phi_{I,J}.
 \tag{21}
\]
For \(R=d\), \(S_N=0\) and \(h_N^{\rm phys}=0\); no nonexistent
head row is inserted. The case \(R=0\) is also exact: the localized
sum is empty and the outward row supplies the selected period.
In particular a constant profile \(C_a^J\) contributes zero to
(17), although its projected period (15) need not vanish.

The factor \(Q/\rho\), of order \(N\), is precisely C's existing
closing-current factor. It is not an additional copy of the
\((1-Q^{-1})^{-1}\) factor in C's routed description.

All normal rows have an exact prescription before specialization.
With \(\delta=1-Q^N\), \(\gamma=Q^{1-N}\), C's finite identity is
\[
\begin{split}
 \rho\,\Phi(V)
   ={}&\gamma\,\Phi(F[V,Q_{\rm f}])\\
     &+\delta\{\gamma\Phi(FQ_{\rm f}V)
                        -q^{-1}\Phi(P_dV)\}.
\end{split}                                                    \tag{22}
\]
Here \(\Phi(V)=\varkappa\operatorname{Tr}(g_1V)\) in the calibrated
coordinates, with spectators retained; \(V\) is the whole calibrated
word, not the old word with its compensating factors omitted.
Apply it to the calibrated word in (5) and to its projected pieces,
including the compensating \(g_1^{-1}\). Expand the commutator through
the whole ordered word. Off root use
\(g_a=g_0Q^{(N-1)a}\) in (16)'s direct coefficient calculation;
do not differentiate (18) as if \(Q^N=1\) held on a disk.
E's two-wall rows and all projector-edge terms remain. If C's routed
alternative is used, its constant-anchor and tail-pivot terms must
likewise be retained. The auxiliary germ retains the ADO pivot.
The ordinary-color path alone is not an identification with closed
Jones normalizations; its entire pivot/twist adapter is required
before that comparison. No packet estimate for these normals is
asserted below.

## 4. What a neighboring profile must supply

Equations (14) and (18) isolate an exact sufficient input without
requiring a Gaussian. Let \(w_N\to\infty\), \(w_N=o(N)\),
\(R_N=\lfloor Cw_N\rfloor\), and let \(A_N\ne0\) and \(v_N>0\).
Suppose the actual coefficients (14) satisfy
\[
 \sup_{0\le a\le R_N}
 \left|\frac{C_a^{J_N}}{A_Nv_N}
                   -\psi(a/w_N)\right|\longrightarrow0,
 \tag{23}
\]
where \(\psi\) is continuous on \([0,C]\). Then ordinary Riemann
sums and \(Q^{-a}=1+O(w_N/N)\), uniformly there, prove
\[
 \frac{(Q/\rho)J_{I_N,J_N}^{\rm loc}}
             {\varkappa g_0 A_Nv_Nw_N}
       \longrightarrow
             \int_0^C\psi(x)\,dx-C\psi(C).
 \tag{24}
\]
The projected period (15) instead tends to \(\int_0^C\psi(x)\,dx\)
under the same normalization. Their difference is exactly the limit
of the outward row. A nonzero right side of (24) gives a lower bound
for this specified localized current, with its displayed normalization.
It does not bound the sum with the remaining source terms.

For a non-invariant rectangle one additionally needs the actual
outgoing pairing in (12); (23) for a compressed environment does not
control it. An upper donor interval likewise retains the lower
interface value just outside that interval. A fixed number of buffered
rows does not by itself bound transfers arriving from far outside.
These are source conditions, not consequences of Euler invertibility.

## 5. Two conditional coefficient profiles, with the finite sum retained

The following are sufficient hypotheses on (6), in the gauges (13).
They illustrate a calculation the exact kernel performs, rather than
describe the original geometric network. All omitted current/source
pieces remain as in Sections 2--3.
In this section \(x,y\) are scaled occupation coordinates, distinct
from the head parameter \(x=-M/q\) in (1).

### 5.1 Two endpoint zeros

Put \(w=N^{3/4}\), \(I=[0,\lfloor C_1w\rfloor]\),
\(J=[d-\lfloor C_2w\rfloor,d]\), and \(k=d-b\).
The two gauged arrow coefficients are
\[
 t_N(a,d-k)=\frac{\beta_a\beta_{N-k}}h,\qquad
 \beta_a=-4\sin^2(\pi a/N).
 \tag{25}
\]
With \(x=a/w,y=k/w\), Taylor's formula, uniformly on the fixed
rectangle, gives
\[
 t_N(a,d-k)=t(x,y)+O(N^{-1/2}),\qquad
                  t(x,y)=-8\pi^3i\,x^2y^2.
 \tag{26}
\]
Each transfer decreases both \(a\) and \(k\).

Assume, for fixed \(\alpha,\beta>0\), real \(\zeta\), and a fixed
\(D\), that some \(A_N\ne0,\epsilon_N\to0\) satisfy for every
\(a,k\) in the rectangle and every \(0\le n\le\min(a,k)\),
\[
 \left|
 \frac{e_{N,n}(a,d-k)}{A_N}
            -\zeta^n e^{-\alpha x^2-\beta y^2}\right|
                      \le\epsilon_N D^n.
 \tag{27}
\]
This is a hypothesis on actual shifted environment entries, including
their phases. It is stronger than a norm bound or a positive Hessian.

The exact transfer sum in (14), before summation over \(k\), then obeys
\[
\begin{split}
 &\frac1{A_N}\sum_{n=0}^{\min(a,k)}
       e_{N,n}(a,d-k)\gamma_{N,n}^{\varepsilon}
                              t_{N,n}(a,d-k)\\
 &\qquad=e^{-\alpha x^2-\beta y^2+\varepsilon\zeta t(x,y)}
                         +O(\epsilon_N+N^{-1/2}+w^{-1}+N^{-1}).
\end{split}                                                    \tag{28}
\]
The error is uniform on the whole closed rectangle, including its
zero-occupation sides. To verify this without an infinite-transfer
replacement, all allowed one-step coefficients are bounded by a fixed
constant. Before the first zero, (26) and the Lipschitz bound for
\(t(x,y)\) give a product error at most
\[
 C_0^n n^2(N^{-1/2}+w^{-1}).
 \]
If a transfer would pass the first zero, set its actual product to
zero. At the zero step the same Lipschitz estimate bounds the
constant-product discrepancy; the telescoping argument still applies.
For example, if \(n>a\), \(x<n/w\), so the vanishing donor factor
has the required bound. Sum these estimates, (3), and (27) against
the factorial majorant. The remaining exponential series beyond
\(n=N-1\) is \(O(N^{-1})\) on this fixed rectangle. This proves
(28) from the original finite sum.

Consequently (23) holds with \(v_N=w\) and
\[
 \psi_{C_2}(x)=
 e^{-\alpha x^2}
       \int_0^{C_2}e^{-(\beta+\varepsilon8\pi^3i\zeta x^2)y^2}\,dy.
 \tag{29}
\]
There are fixed, sufficiently large \(C_1,C_2\) for which the
right side of (24) is nonzero for this profile. Indeed as
\(C_2\to\infty\),
\[
 \psi_\infty(x)=
 \frac{\sqrt\pi\,e^{-\alpha x^2}}
                     {2\sqrt{\beta+\varepsilon8\pi^3i\zeta x^2}},
 \tag{30}
\]
with the square root having positive real part. Its argument lies
between \(-\pi/4\) and \(\pi/4\). Hence its integral on the positive
half-line has positive real part. Choose \(C_1\) large enough that
the Gaussian tail and \(C_1\psi_\infty(C_1)\) do not cancel that
integral, then \(C_2\) large enough. Uniform convergence on
\([0,C_1]\) follows from the majorant \(e^{-\beta y^2}\).
This proves conditional nonvanishing of the localized current.

### 5.2 One endpoint zero

Use \(G_F\otimes1\), \(w=\sqrt N\), \(I=[0,\lfloor Cw\rfloor]\),
and retain the whole recipient head. Fix \(t_0\in(0,1)\),
\(b_0=\lfloor t_0N\rfloor\), \(B=e^{2\pi it_0}\), and put
\(x=a/w,y=(b-b_0)/w\). Here
\[
 t_N(a,b)=\beta_a(1-Q^{b+1})/h
               \longrightarrow 2\pi i(1-B)x^2
 \tag{31}
\]
on bounded \(x,y\) sets.
Assume that fixed \(\zeta\in\mathbb C,D>0\), nonzero \(A_N\), and
\(\epsilon_N\to0\) give, for all physical \(b\) and allowed
\(n\le\min(a,d-b)\),
\[
 \left|\frac{e_{N,n}(a,b)}{A_N}
          -\zeta^n e^{-\alpha x^2-\beta y^2}\right|
                  \le\epsilon_N D^n e^{-\beta_0y^2},
 \tag{32}
\]
where \(\alpha,\beta,\beta_0>0\), \(\epsilon_N\to0\), and
\[
          \Re\Lambda>0,\qquad
       \Lambda=\alpha-\varepsilon2\pi i(1-B)\zeta .
 \tag{33}
\]
The whole-recipient tail bound in (32) is essential.

The proof of (28), followed by the recipient Riemann sum, now gives
(23) with \(v_N=w\) and
\[
                     \psi(x)=\sqrt{\pi/\beta}\,e^{-\Lambda x^2}.
 \tag{34}
\]
For detail, the one-step error from (31) is bounded on the whole
physical head by \(C(1+|y|)/w\), and the transfer-shift error by
\(Cn/w\) before a forced zero. The coefficients remain uniformly
bounded everywhere on this donor collar. Their factorial sums are
therefore dominated by a fixed multiple of
\((1+|y|)e^{-\beta_1y^2}\), with
\(\beta_1=\min(\beta,\beta_0)>0\).
The physical recipient endpoints tend to \(y=\pm\infty\);
their omitted Gaussian tails vanish. At a forced upper zero the
same telescoping estimate applies, or its exponentially small
recipient tail bounds the discrepancy. This proves the asserted
uniform donor profile and retains the actual upper projector.
Since \(\Re\Lambda>0\),
\(\int_0^\infty\psi(x)\,dx\ne0\), while \(C\psi(C)\to0\).
Thus (24) is again nonzero for sufficiently large fixed \(C\).

## 6. What has and has not been matched

The exact statements (5), (10), (12), (14), and (18)--(22) apply
to the original marked finite source. All local normal identities
are retained before specialization. The conditional limits use only
the root fiber and add no uniform packet claim for meridian or
quantum normals.

The universal scales are \(\sqrt N\) for one vanishing endpoint
factor and \(N^{3/4}\) for two. Their endpoint gauges have E's
subexponential condition numbers, but the packet hypotheses are
stated after that exact source transformation. They are not implied
by bounds in an unrelated norm.
The amplitudes \(A_N\) retain all source normalization; no polynomial
power or exponential rate for them has been assumed or deduced.
Neither (24) nor its Gaussian instances proves that the complementary
current has a smaller rate or cannot cancel the displayed contribution.
The exact interface formula also applies to correlated profiles once
the actual neighboring network supplies (23).

## Complete proof-source pins

* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.
* C: notes/research_routed_residue_cut_current_adapter.md,
  SHA256 f6e634b156ac6f208083243fae6137dc712a25965f5fd77b713bb7b55d21291d.

Both complete direct texts were freshly read nontruncated in this
author sequence and every used implication checked. The older signed
Gaussian endpoint packet was checked for coverage: it concerns the
Casimir/Hermite filling packet, not (10)'s occupation-transfer kernel.
It is not a proof premise. No mathematical programs, tests, or frozen
source edits were used.
