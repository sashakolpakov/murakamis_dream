# Carry-projector Ward decay through an actual fixed braid word

Private written proof, 19 November 2026.

The normalized coherent estimate for a carry-projector current can
be propagated through a literal finite braid word on an explicit
open domain. The proof sums the actual crossing transfers before
estimating the current. It does not multiply normalized coherent
symbols or assume a crossing amplitude is a unit.

The propagation cost is a positive linear map on output moduli.
Its finite composition gives a computable exponential base for the
complete word. On the domain where that base is less than one, all
fixed coherent derivatives and genuine meridian jets of the composed
current decay exponentially. The physical caps, crossing scalars,
and original zero-framing line remain explicit. No assertion places
an arbitrary geometric critical point or closing cycle in this domain.

## 1. Actual matrices and a finite column majorant

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(M=e^\mu\), and \(x=-M/q\). The quantum root is fixed. There
are \(m\ge2\) physical heads with occupations \(0,\ldots,d\).
F supplies the literal arrows
\[
 E(M)e_a=(MQ^{-a}-M^{-1})e_{a-1}\quad(a>0),\quad E(M)e_0=0,
 \qquad Fe_a=(1-Q^{a+1})e_{a+1},\quad Ke_a=xQ^{-a}e_a.
 \tag{1}
\]
The upper \(F\) arrow is zero. Write \(f_a=(Q;Q)_a\), and remove
only the actual common crossing scalar by setting
\(\widehat R^\sigma(M)=\kappa(M)^{-\sigma}R^\sigma(M)\),
\(\sigma=\pm1\). The finite matrices of F(31) are
\[
 \widehat R^+=PD\sum_{n=0}^{d}
       \frac{(-1)^nq^{n^2}}{f_n}E_1^nF_2^n,
 \qquad
 \widehat R^-=\sum_{n=0}^{d}\frac{q^n}{f_n}E_1^nF_2^nD^{-1}P,
 \tag{2}
\]
where \(P\) flips the heads and
\(De_{a,b}=x^{-a-b}Q^{ab}e_{a,b}\).
These are physical finite matrices, not cyclic completions.

At \(M=1\), every nonzero positive entry has output
\((b+n,a-n)\), \(0\le n\le\min(a,d-b)\). The negative entry
has output \((b-n,a+n)\), \(0\le n\le\min(b,d-a)\).
The donor product in (2) satisfies
\[
 \prod_{j=a-n+1}^{a}(Q^{-j}-1)
       =Q^{-n(2a-n+1)/2}\frac{f_a}{f_{a-n}}.
 \tag{3}
\]
Thus the positive coefficient, up to a modulus-one phase, is
\({a\brack n}_Q\prod_{j=b+1}^{b+n}(1-Q^j)\).
For the negative coefficient it is
\({b\brack n}_Q\prod_{j=a+1}^{a+n}(1-Q^j)\).
All the displayed factorial indices are below \(N\).

The finite Gaussian polynomial has nonnegative coefficients with
sum \(\binom an\): induction in
\({a\brack n}_Q={a-1\brack n}_Q+
Q^{a-n}{a-1\brack n-1}_Q\) proves both statements, including
the endpoint polynomials one. Consequently, at every level,
\[
 |(\widehat R^+_0)_{b+n,a-n;\,a,b}|\le\binom an2^n,
 \qquad
 |(\widehat R^-_0)_{b-n,a+n;\,a,b}|\le\binom bn2^n.
 \tag{4}
\]
Here the subscript zero means \(M=1\). Extending the nonnegative
majorant sum beyond an actual recipient cap only enlarges a bound;
no forbidden matrix entry is introduced into (2).

For nonnegative output weights \(s_1,s_2\), summing every actual
transfer in (4) gives
\[
 \begin{split}
 \sum_{c,e}|(\widehat R^+_0)_{c,e;\,a,b}|s_1^cs_2^e
       &\le(s_2+2s_1)^a s_1^b,\\
 \sum_{c,e}|(\widehat R^-_0)_{c,e;\,a,b}|s_1^cs_2^e
       &\le s_2^a(s_1+2s_2)^b.
 \end{split} \tag{5}
\]
The binomial theorem proves these inequalities also at zero weights,
with \(0^0=1\). No division by \(s_1\) or \(s_2\) is used.

For a pair at positions \(i,i+1\), define the nonnegative linear
maps \(\mathsf U_{i,\sigma}\) by leaving every other coordinate
fixed and replacing that pair by
\[
 \mathsf U_+(s_1,s_2)=(s_2+2s_1,s_1),\qquad
 \mathsf U_-(s_1,s_2)=(s_2,s_1+2s_2).
 \tag{6}
\]
They are majorants for the signed matrices, not inverse maps or
classical braid maps.

## 2. Word composition and the true meridian collar

Let the fixed word act as
\[
 W_\beta(M)=R_{i_c}^{\sigma_c}(M)\cdots R_{i_1}^{\sigma_1}(M),
 \qquad \omega=\sum_{\ell=1}^c\sigma_\ell,\qquad
 \widehat W_\beta=\kappa(M)^{-\omega}W_\beta.
 \tag{7}
\]
Given an output weight vector \(s\ge0\), define recursively
\[
 s^{(c)}=s,\qquad
 s^{(\ell-1)}=\mathsf U_{i_\ell,\sigma_\ell}(s^{(\ell)}),
 \qquad U_\beta(s)=s^{(0)}.
 \tag{8}
\]
The order in (8) is backwards through the actual ordered product.
Taking absolute values of the finite matrix product, summing its
last output first, and applying (5) inductively proves
\[
 \sum_{\mathbf b}|(\widehat W_\beta(1))_{\mathbf b,\mathbf a}|
                    s^{\mathbf b}
       \le \prod_{j=1}^m U_{\beta,j}(s)^{a_j}.
 \tag{9}
\]
Every intermediate sum still uses \(0\le a_j\le d\).

This estimate extends to the actual complex meridian family.
For \(0<\eta'<\pi\), F(25),(32) supply the diagonal matrices
\[
 D_h(M)e_a=h_a(M)e_a,\qquad
 h_a(M)=M^{-a}\frac{f_a}{(M^{-2}Q;Q)_a},\qquad
 \|D_h^{\pm1}\|\le(N+1)^{C_{\eta'}}
 \tag{10}
\]
on \(|N\mu|\le\eta'\), and the exact identities
\[
 \begin{split}
 \widehat R_i^+(M)
   &=M^{-J_i-J_{i+1}}D_{h,i+1}(M)
                 \widehat R_{i,0}^+D_{h,i}(M)^{-1},\\
 \widehat R_i^-(M)
   &=M^{J_i+J_{i+1}}D_{h,i}(M)
                 \widehat R_{i,0}^-D_{h,i+1}(M)^{-1}.
 \end{split} \tag{11}
\]
All frames and their inverses are holomorphic on that collar.
For each entry, their absolute cost is at most a power of \(N\),
and \(|M|^{\pm(J_i+J_{i+1})}\le e^{2\eta'}\).
Applying (5) with these bounds at every original stage proves
\[
 \boxed{\quad
 \sum_{\mathbf b}|(\widehat W_\beta(e^\mu))_{\mathbf b,\mathbf a}|
                    s^{\mathbf b}
       \le C(N+1)^B\prod_j U_{\beta,j}(s)^{a_j},
       \qquad |N\mu|\le\eta'.
 \quad} \tag{12}
\]
The constants depend on the fixed word and collar, not on its
occupations, the output weights, or the level. No adjacent frames
were cancelled and no off-root factorial reflection was used.

## 3. The complete composed threshold kernels

For any actual matrix on the \(m\) heads, use the input-binomial
kernel
\[
 K_A(z,w)=\sum_{\mathbf a,\mathbf b}
       A_{\mathbf b,\mathbf a}
       \prod_j\binom d{a_j}z_j^{b_j}w_j^{a_j},\qquad
 I_N(z,w)=\prod_j(1+z_jw_j)^d.
 \tag{13}
\]
All its sums are finite. Fix an adjacent pair \(p,r=p+1\), and put
\[
 E_{pr}=E_pK_r+E_r,\quad F_{pr}=F_p+K_p^{-1}F_r,
 \quad J_{pr}=J_p+J_r,\quad
 \Pi_0=\mathbf1_{J_{pr}\le d},\quad\Pi_1=I-\Pi_0.
 \tag{14}
\]
Define the normalized composed currents
\[
 \mathcal E_{\beta,p}=
       \frac{K_{\widehat W_\beta E_{pr}\mathbf1_{J_{pr}=N}}}{I_N},
 \qquad
 \mathcal F_{\beta,p}=
       \frac{K_{\widehat W_\beta F_{pr}\mathbf1_{J_{pr}=d}}}{I_N}.
 \tag{15}
\]
The current acts first, immediately before the displayed word.
Assume only \(1+z_jw_j\ne0\). Write
\[
 U=U_\beta(|z|),\quad X_j=U_j|w_j|,\quad
 \mathcal B_{\beta,p}(z,w)=
 \frac{(\sqrt{X_p}+\sqrt{X_r})^2
                \prod_{j\ne p,r}(1+X_j)}
      {\prod_j|1+z_jw_j|}.
 \tag{16}
\]
Then for the same buffered collar as in (12),
\[
 \boxed{\begin{split}
 |\mathcal E_{\beta,p}|
    &\le C(N+1)^B d(|w_p|+|w_r|)\mathcal B_{\beta,p}^{d},\\
 |\mathcal F_{\beta,p}|
    &\le C(N+1)^B(U_p+U_r)\mathcal B_{\beta,p}^{d}.
 \end{split}} \tag{17}
\]
In particular the estimate includes zero output coordinates.

Here is the complete contraction proof. On input pair occupations
\((a,b)\), \(E_{pr}\) has coefficients
\(xQ^{-b}(MQ^{-a}-M^{-1})\) and \(MQ^{-b}-M^{-1}\), and
lowers the first or second occupation. On the threshold \(a+b=N\)
both occupations are positive, so neither bottom arrow is added.
The coefficients are bounded on the collar. Equation (12) thus
weights the two terms by \(U_p^{a-1}U_r^b\) and
\(U_p^aU_r^{b-1}\), respectively.
For \(F_{pr}\), on \(a+b=d\), the analogous weights are
\(U_p^{a+1}U_r^b\) and \(U_p^aU_r^{b+1}\), with bounded
coefficients \(1-Q^{a+1}\) and \(x^{-1}Q^a(1-Q^{b+1})\).
Their actual upper zeros remain in the finite sum.

For clarity let
\(S_\ell(X,Y)=\sum_{a+b=\ell}\binom da\binom dbX^aY^b\).
The positive-coefficient estimate
\[
 S_\ell(X,Y)\le R^{-\ell}(1+RX)^d(1+RY)^d
 \tag{18}
\]
with \(R=(XY)^{-1/2}\) gives
\(S_d\le(\sqrt X+\sqrt Y)^{2d}\).
Moreover \(S_N\) is divisible by \(XY\), and reindexing \(a-1\)
with \(\binom da\le d\binom{d-1}{a-1}\) gives
\[
 S_N(X,Y)/X\le d(\sqrt X+\sqrt Y)^{2d},\qquad
 S_N(X,Y)/Y\le d(\sqrt X+\sqrt Y)^{2d}.
 \tag{19}
\]
These are precisely C's divided-shell estimates, with their proof
unchanged when the denominator is the original \(I_N\).
Continuity of the polynomial quotients gives (19) also at zero.

In the first lowering term, \(|w_p|\) times \(S_N/X_p\)
is the weighted pair sum; the other term uses \(|w_r|S_N/X_r\).
For the raising terms the factors are \(U_pS_d,U_rS_d\).
Every spectator sum is exactly \((1+X_j)^d\).
Multiplication of these bounds and division by \(|I_N|\) proves
(17). The argument estimates the full finite composition, including
all its transfers, before any normalized kernel is formed.

## 4. An explicit open domain, jets, and original scalar lines

Let \(\mathcal K\) be a compact subset of
\[
 \mathcal V_{\beta,p}=
   \{(z,w):1+z_jw_j\ne0\text{ for all }j,
                       \mathcal B_{\beta,p}(z,w)<1\}.
 \tag{20}
\]
This is a nonempty open set for every fixed word. Indeed take
\(z_j=w_j=t>0\). By homogeneity of (6),(8), write
\(U_\beta(t\mathbf1)=t\,a\), where every \(a_j>0\) is fixed.
Then
\[
 \mathcal B_{\beta,p}(t\mathbf1,t\mathbf1)
   =t^2(\sqrt{a_p}+\sqrt{a_r})^2
       \frac{\prod_{j\ne p,r}(1+a_jt^2)}{(1+t^2)^m}
       \longrightarrow0.
 \tag{21}
\]
Choose one sufficiently small positive \(t\), independent of
\(N\), and a complex neighborhood of it. Its binomial input mean
on every head is \(dt^2/(1+t^2)\), an extensive positive occupation;
the domain is not restricted to the vacuum point.

Choose \(0<\eta<\eta'<\pi\). Compactness supplies a fixed complex
neighborhood of \(\mathcal K\) with bounded coordinates, nonzero
incidence denominators, and \(\mathcal B_{\beta,p}\le\gamma<1\).
The kernels (15) are holomorphic there and on the buffered meridian
collar. Apply (17) on that neighborhood, then Cauchy's formula in
the coordinates and in \(u=N\mu\). For every fixed multi-index
\(\alpha\) and integer \(k\ge0\),
\[
 \sup_{\substack{(z,w)\in\mathcal K\\|N\mu|\le\eta}}
 \left(|\partial_{z,w}^{\alpha}\partial_\mu^k\mathcal E_{\beta,p}|
       +|\partial_{z,w}^{\alpha}\partial_\mu^k\mathcal F_{\beta,p}|\right)
       \le C_{\alpha,k,\mathcal K,\eta,\eta'}
                    (N+1)^{B+k+1}\gamma^d.
 \tag{22}
\]
Thus these actual composed currents and all the stated jets are
exponentially small. The \(N^k\) cost is the true meridian cost
\(\partial_\mu=N\partial_u\); all moving crossing frames are
differentiated. No derivative of a root-only expression is substituted.

The raw word in (7) retains the scalar \(\kappa(M)^\omega\).
For it the exact current is \(\kappa^\omega\) times (15), and
every derivative retains the full product rule. For the standard
zero-framed word, H(16) gives
\[
 \alpha=\kappa x^{-d},\qquad
 \overline W_\beta=\alpha^{-\omega}W_\beta
                   =x^{d\omega}\widehat W_\beta.
 \tag{23}
\]
The last scalar is bounded by \(e^{|\omega|\eta'}\) on the collar;
its derivative of order \(j\) is \((d\omega)^j x^{d\omega}\).
Hence (22) holds for the actual zero-framed composed current as
well. Prescribed further scalar lines remain multiplied in their
original positions; the same exponential conclusion for them needs
their stated buffered subexponential bounds, not a scalar reset.

Fixed integer Cartan powers inserted beside the current also obey
(17),(22). They multiply its finitely many arrow coefficients by
unit \(Q\)-phases and fixed Laurent powers of \(M\). This includes
the spectator Cartans in the total coproduct currents below.

## 5. Two-sided transport of every internal threshold

A coarser estimate covers a current at an arbitrary internal seam,
with actual finite word factors on both sides. Let \(A(M),B(M)\)
be fixed products of stripped crossings and the degree projectors
(14), and let \(c\) be their total number of crossings. Put
\[
 C_E=[E_\Sigma,\Pi_0],\qquad C_F=[F_\Sigma,\Pi_0],
 \qquad
 \mathcal J_E=\frac{K_{A C_E B}}{I_N},\quad
 \mathcal J_F=\frac{K_{A C_F B}}{I_N}.
 \tag{24}
\]
The threshold pair may be any adjacent pair. Let
\[
 s=\max_j|z_j|,\quad t=\max_j|w_j|,\quad \tau=st,
 \qquad C_m=\frac{m^m}{(m-1)^{m-1}},\qquad
 \Omega_{m,c}(\tau)=\frac{3^c C_m\tau}{(1-\tau)^m}.
 \tag{25}
\]
For \(0\le\tau<1/(m-1)\), the following actual kernel bounds hold
on the buffered meridian collar:
\[
 |\mathcal J_E|\le C(N+1)^{B_0}(m-1)t\,\Omega_{m,c}(\tau)^d,
 \qquad
 |\mathcal J_F|\le C(N+1)^{B_0}s\,\Omega_{m,c}(\tau)^d.
 \tag{26}
\]
Fixed compact sets of phase marks \(\Pi_0+\zeta\Pi_1\) may
also replace any of the inserted projectors; only the constant
changes. These marks need not intertwine the total arrows.

To prove (26), first set both weights in (5) equal to one. Each
root crossing has maximum input-column sum at most \(3^d\).
Equation (11) preserves this up to a collar-uniform polynomial
factor. Every inserted degree projector has column norm at most
one. The total-current matrices \(C_E,C_F\) have bounded column
norm on the collar, since (1) and the fixed coproduct have bounded
arrow coefficients. Therefore
\[
          \|A C_E B\|_1+\|A C_F B\|_1
                    \le C(N+1)^{B_0}3^{cd}.
 \tag{27}
\]
Here \(\|\cdot\|_1\) is the maximum absolute input-column sum,
not a coherent-kernel norm. Each crossing and each projector
preserves the global integer degree \(J_{\rm all}=\sum_jJ_j\).
A nonzero \(C_E\) input has pair degree \(N=d+1\), hence global
degree at least \(d+1\), and its output degree is one lower.
A nonzero \(C_F\) input has pair degree \(d\), and its output
degree is one higher. These support statements remain true with
\(B\) before the current and \(A\) after it.

For \(s,t>0\), (27) consequently bounds the absolute coherent
numerators by
\[
 \begin{split}
 C(N+1)^{B_0}3^{cd}s^{-1}
        \sum_{J\ge d+1}\binom{md}{J}\tau^J,
 \qquad
 C(N+1)^{B_0}3^{cd}s
        \sum_{J\ge d}\binom{md}{J}\tau^J,
 \end{split} \tag{28}
\]
respectively. The coefficient \(\binom{md}{J}\) is the exact
Vandermonde sum of all input binomial weights at total degree
\(J\). No independence of the intervening occupations is assumed.
For \(R>1\), the degree tail beginning at \(l\) is at most
\(R^{-l}(1+R\tau)^{md}\). Choose
\(R=((m-1)\tau)^{-1}\). The two tails in (28) are at most
\((m-1)\tau(C_m\tau)^d\) and \((C_m\tau)^d\).
Finally \(|I_N|\ge(1-\tau)^{md}\). Substitution proves (26),
including the factor \(s^{-1}\tau=t\) in its first bound.
At \(\tau=0\), both actual kernels vanish by the stated total
degree support, and (26) follows by continuity.

The domain \(\Omega_{m,c}(\tau)<1\), within the preceding
\(\tau\)-range, contains a nonempty polydisc about the origin
and fixed positive points in it. On every compact subset, a fixed
complex buffer gives \(\Omega_{m,c}\le\gamma<1\). The same
holomorphy and Cauchy argument as in (22) proves exponential decay
of all fixed mixed coherent and true meridian jets of (24), with
only polynomial \(N\)-cost. The scalar restoration (23) applies
unchanged. This result estimates literal two-sided compositions;
it makes no assertion about arbitrary matrices of uncontrolled
degree support or column norm.

## 6. The exact Ward row and the remaining source scope

For \(Z_{pr}=\Pi_0+\zeta\Pi_1\), C's literal degree identities are
\[
 [E_{pr},Z_{pr}]=(\zeta-1)E_{pr}\mathbf1_{J_{pr}=N},\qquad
 [F_{pr},Z_{pr}]=(1-\zeta)F_{pr}\mathbf1_{J_{pr}=d}.
 \tag{29}
\]
Thus (17),(22) estimate the corresponding actual rows
\(\widehat W_\beta[E_{pr},Z_{pr}]\) and
\(\widehat W_\beta[F_{pr},Z_{pr}]\), uniformly for \(\zeta\)
in a fixed compact set. With the ordered total coproducts of F(8),
\[
 [E_\Sigma,Z_{pr}]=[E_{pr},Z_{pr}]\prod_{j>r}K_j,
 \qquad
 [F_\Sigma,Z_{pr}]=\left(\prod_{j<p}K_j^{-1}\right)
                                      [F_{pr},Z_{pr}].
 \tag{30}
\]
Terms outside the pair commute with its degree projector; within
the pair, the indicated Cartan factors give (30) directly.
For the actual braid intertwiners these are also the full rows
\([E_\Sigma,W_\beta Z_{pr}]=W_\beta[E_\Sigma,Z_{pr}]\) and
the analogous \(F_\Sigma\) row, with their original scalar.
For completeness, this intertwining can be checked in the finite
sum (2). Let \(\Theta=\sum_n c_nE_1^nF_2^n\) denote its positive
Euler factor. The arrows (1) give
\[
 [E,F^{n+1}]=-q^{-1}Q^{-n}(1-Q^{n+1})F^n(K-Q^nK^{-1}).
 \tag{31}
\]
Together with
\(c_{n+1}/c_n=-q^{2n+1}/(1-Q^{n+1})\), this cancels consecutive
coefficients of \(E_1^{n+1}F_2^n\) and proves
\[
 \Theta(E_1K_2+E_2)=(E_1K_2^{-1}+E_2)\Theta,
 \qquad
 \Theta(F_1+K_1^{-1}F_2)=(F_1+K_1F_2)\Theta.
 \tag{32}
\]
The second identity follows by the same adjacent-transfer comparison.
Conjugating the right-hand expressions by \(D\) and then flipping
the heads gives the original coproduct. At the top of the finite
comparison the residual has \(E_1^N\) or \(F_2^N\), which is zero;
the lower comparison uses the actual bottom-zero arrow. This proves
the positive intertwining, and its actual inverse proves the negative
one. No cyclic endpoint is used in this Ward interpretation.

In particular a carry-sector word
\(W_{\beta,\mathbf b}=(R_{i_c}^{\sigma_c}\Pi_{i_c,b_c})
\cdots(R_{i_1}^{\sigma_1}\Pi_{i_1,b_1})\) has a total Ward
commutator equal to the finite Leibniz sum over its projector
slots. Each summand has the form in (24), with exactly \(c\)
crossings between its two sides and with the other projectors
retained. After stripping the common scalar, (26) and its jet bounds
estimate every such internal current and their sum, uniformly over
the finite sector set. The same holds after zero-framing restoration
(23); the raw scalar retains its displayed product rule. This does
not use sectorwise scalar-cut identities.

The usual donor-Gaussian column estimate already appears in
ordinary-color coefficient bounds. The conclusion here is its
specific finite composition with a threshold current in the actual
balanced meridian family, giving (16)--(22) and the two-sided bounds
(24)--(28) on explicit nonempty complex coherent domains.
The original Newton/Fourier identities for one or
two negative crossings and the q-Hahn local amplitudes concern
different kernels; none is used as a proof premise here.

The bound is on the original composed kernel divided by its stated
identity kernel. It is not relative to a possibly vanishing kernel
of \(W_\beta\), and it is not an exponentially small operator norm.
The two-sided theorem covers actual fixed word/projector products,
including every internal sector current. A separate contracted
boundary state cannot be renamed as a free binomial column without
estimating its actual adapter. Applying these bounds to the closing
source still requires a contour and bounds on its remaining density
and boundary currents. No geometric membership of these domains,
cycle coefficient, or noncancellation of the original closed scalar
is inferred.

## Complete proof directs

* C: `notes/research_carry_projector_ward_decay.md` (236 lines),
  SHA256 `6aec272af36618cb3f13ab40b2fa539a6c5d8f5ad40d8688206f7a3f3a806829`.
* F: `notes/research_actual_meridian_source_frames.md` (506 lines),
  SHA256 `6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976`.
* H: `notes/research_actual_meridian_hankel_transport.md` (271 lines),
  SHA256 `e50f4257e3464863167d8a04c060753d937921d27c551d8ee18f882add1111e9`.

All complete directs were whole-read nontruncated in this active
sequence. The proof uses only written finite calculations and
text/hash operations. Frozen and public files were not edited.
