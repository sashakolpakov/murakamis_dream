# Exact Fourier propagation through the next attachment

Private finite-source deduction, 9 November 2026. The full right
remainder of the adopted \(343\) transfer can be attached once more
before any absolute value is taken. Its inner Fourier observations
are unchanged. The outgoing coefficient is a specified two-step
conditional polynomial, with the same positive Newton-to-Chebyshev
transition and all its original complex phases.

The previous triangular degree bound in the outgoing variable is
not preserved. This is visible in an actual nonzero coefficient,
not only in a norm on arbitrary inputs. The formulas below identify
the endpoint observation that supplies its new top degree. They do
not estimate the new complete conditional cycle or assert propagation
of the geometric remainder gap. The task attachment was reread.
No mathematical numerical evaluation, import, compilation, or
frozen-source edit is used.

## 1. The exact next operator

Put
\[
\begin{gathered}
D=N-1,\quad N\ge6,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
\kappa=q^{D^2/2},\\
P_j=(r;r)_j,\qquad p_j(Z)=(rZ;r)_j,\qquad
C_{\beta,N}(Y,W)=
 \sum_{j=0}^D\frac{Y^{-j}p_j(Y)p_j(W)}{P_j^{2+\beta}},
 \qquad\beta\in\{0,1\}.
\end{gathered}                                                     \tag{1}
\]
Every denominator in (1) is nonzero. The literal products retain
their physical support zeros. For a polynomial \(f\) of degree at
most \(D\), define
\[
(\mathsf T_{0\beta}f)(W)
 =\sum_{a=0}^Df(r^a)C_{\beta,N}(r^a,W)
 =N\operatorname{CT}_Z[f(Z)C_{\beta,N}(Z,W)] .
                                                                    \tag{2}
\]
The constant term is the integral on any counterclockwise circle
about zero, with measure \(dZ/(2\pi iZ)\). The \(Z\)-band of its
integrand is contained in \([-D,D]\), so only frequency zero
survives root averaging.

Equation (2) is the next normalized transfer after a last letter
three. There is no old-four factor \(d_N(Z)(1+Z^{-N})\).
If the new letter is four, its factorial is already present as
\(P_j^{-3}\) in \(C_{1,N}\); the old variable in (2) is still
unweighted. This is the exact convention of
[torus composition, (1)--(3) and (18)--(20)](research_mixed_conditional_torus_composition.md).

Let \(T_N(w,Z)\) be the full \(343\) message. In the
[original message bridge, (4), (7), and (9)](research_mixed_conditional_fourier_message_bridge.md),
the entire new message
\[
F^{(4)}_{\beta,N}(w,W)=\mathsf T_{0\beta}[T_N(w,\cdot)](W)
                                                                    \tag{3}
\]
satisfies
\[
\mathcal E_\beta F^{(4)}_{\beta,N}
 =\frac{v(w)^TA_3A_4A_3A_{3+\beta}h}
             {\kappa^{5+\beta}N^{1+\beta}} .
                                                                    \tag{4}
\]
Thus no additional crossing scalar belongs inside (2). All
ordinary derivatives differentiate the original \(v(w)\) and the
same complete finite source.

For a fixed base contour the
[adopted bidisk transfer, (6)--(8)](research_mixed_next_transfer_complex_neighborhood.md)
has the exact decomposition
\[
T_N=I_N+E_N^-+\mathcal R_N^+ .
                                                                    \tag{5}
\]
Here \(I_N\) is its original fixed local incoming integral.
Its output dependence is entirely through the finite \(C_0\);
hence \(I_N\), \(E_N^-\), and \(\mathcal R_N^+\) each have degree
at most \(D\) in \(Z\). Linearity gives the exact full-cycle
identity
\[
F^{(4)}_{\beta,N}
 =\mathsf T_{0\beta}I_N+\mathsf T_{0\beta}E_N^-
                     +\mathsf T_{0\beta}\mathcal R_N^+ .
                                                                    \tag{6}
\]
The exponential bounds for the last two summands before applying
\(\mathsf T_{0\beta}\) hold on their proved output neighborhoods.
Equation (6) does not extend those estimates to the complete
cycle in (2).

## 2. The complete two-step conditional source

Define a single finite Laurent polynomial by
\[
\begin{split}
C^{(2)}_{0\beta,N}(Y,W)
 &=N\operatorname{CT}_Z
       [C_{0,N}(Y,Z)C_{\beta,N}(Z,W)]\\
 &=\sum_{a=0}^D
       C_{0,N}(Y,r^a)C_{\beta,N}(r^a,W).
\end{split}                                                       \tag{7}
\]
It has \(Y\)-band \([-D,0]\) and \(W\)-degree at most \(D\).
There is no choice of off-grid interpolation in (7).
The second equality follows from the same band argument as (2).

The following all-row formula is sometimes useful for identifying
which source has to be estimated:
\[
\boxed{\quad
C^{(2)}_{0\beta,N}(Y,W)
 =\sum_{\ell,j=0}^D
   \frac{Y^{-\ell}p_\ell(Y)p_j(W)}
        {P_\ell P_j^{1+\beta}}\,
                  C_{0,N}(r^j,r^\ell).
\quad}                                                           \tag{8}
\]
Indeed the original shared-node identity is
\[
\sum_{a=0}^D r^{-aj}p_\ell(r^a)p_j(r^a)
                     =P_\ell P_j C_{0,N}(r^j,r^\ell).
                                                                    \tag{9}
\]
On \(\ell+a<N\) and \(j+a<N\), both sides of (9) have
summand
\[
r^{-aj}\frac{P_{\ell+a}P_{j+a}}{P_a^2};
\]
outside that intersection the relevant numerator product vanishes.
This proves (9), including every boundary index. Expanding the two
kernels in (7) and using (9) gives (8). It is the \(\alpha=0\)
case of [coherent suffix reversal, (3)](research_mixed_coherent_suffix_reversal.md).
At \(Y=r^b\), the outer \(\ell\)-sum in (8) stops exactly at
\(D-b\). Its \(j\)-sum is not thereby stopped at \(D-b\).

For \(\beta=0\) there is also a useful normalization check.
If
\[
K_{ab}=C_{0,N}(r^a,r^b),\qquad
\mathsf U=\operatorname{diag}((-q)^{-a}),\qquad
\mathsf H=\mathsf M^*\mathsf M
\]
with \(\mathsf M\) the original crossing matrix, then
[the exact Gram identity, (6)](research_mixed_next_actual_forcing_gram_bounds.md)
gives
\[
\bigl(C^{(2)}_{00,N}(r^a,r^b)\bigr)_{a,b=0}^D
       =K^2=\mathsf U\mathsf H^2\mathsf U^* .
                                                                    \tag{10}
\]
This is an identity of the complete physical matrix. It does not
turn an arbitrary incoming row and its prescribed outgoing
observation into a positive quadratic form.

## 3. The same inner observations, with new exact coefficients

Use
\[
M=\lceil N/2\rceil,\qquad U=\lfloor N/2\rfloor-1=D-M,
\qquad S_j=\prod_{h=1}^j2\sin(\pi h/N),\quad S_0=1 .
                                                                    \tag{11}
\]
Thus \(S_j=|P_j|\), and \(S_D=N\). Put
\[
P_b^{\rm rad}(X)=e_b(X)/e_M(X)\qquad(M\le b\le D).
\]
These are ordinary polynomials, not meromorphic functions.

Keep the full Hermite observation of
[the incoming-color upper theorem, (1)--(6)](research_mixed_next_incoming_color_outer_upper_bound.md):
\[
\begin{split}
Q_{N,w}^{\rm full}(X)
 &=\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N(x,X)],\\
\mathcal O_{N,k}(w)
 &=\phi_N^{(X)}[R_N(X)^3e_M(X)Q_{N,w}^{\rm full}(X)
                                         T_k(-X/2)] .
\end{split}                                                       \tag{12}
\]
In particular every original first normal and the odd simple node
remain in (12).

The exact complete outgoing polynomial and right remainder are
\[
\begin{split}
F_N^+(X,Z)
 &=\sum_{b=M}^D(-q)^b C_{0,N}(r^b,Z)P_b^{\rm rad}(X)
   =\sum_{k=0}^Uf_{k,N}(Z)T_k(-X/2),\\
\mathcal R_N^+(w,Z)
 &=\frac1{\kappa^2N}\sum_{k=0}^U
                           f_{k,N}(Z)\mathcal O_{N,k}(w).
\end{split}                                                       \tag{13}
\]
Define the new coefficients by applying the whole operator:
\[
f^{(2,\beta)}_{k,N}(W)
       =(\mathsf T_{0\beta}f_{k,N})(W).
                                                                    \tag{14}
\]
Then finite linearity proves
\[
\boxed{\quad
(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)
 =\frac1{\kappa^2N}\sum_{k=0}^U
                   f^{(2,\beta)}_{k,N}(W)\mathcal O_{N,k}(w).
\quad}                                                           \tag{15}
\]
Equivalently its inserted polynomial is
\[
F_N^{+,(2,\beta)}(X,W)
 =\sum_{b=M}^D(-q)^b C^{(2)}_{0\beta,N}(r^b,W)P_b^{\rm rad}(X)
 =\sum_{k=0}^Uf^{(2,\beta)}_{k,N}(W)T_k(-X/2).
                                                                    \tag{16}
\]
No cutoff or transformed forcing has been subtracted in (15)--(16).

Let \(\beta_{d,k,N}>0\), \(0\le k\le d\le U\), denote precisely
the weights in
[the positive transition theorem, (6), (10), and (14)](research_mixed_next_outgoing_positive_chebyshev_transition.md).
Then the same exact transition gives
\[
\boxed{\quad
f^{(2,\beta)}_{k,N}(W)
 =(-1)^{M+k}\sum_{d=k}^U
     q^{M+d}\beta_{d,k,N}
                    C^{(2)}_{0\beta,N}(r^{M+d},W).
\quad}                                                           \tag{17}
\]
Only the conditional polynomial has changed. The weights retain
their proved endpoint-uniform entropy, but the complex phase of
\(C^{(2)}\) in (17) has not been removed.

The reversible odd difference also commutes with this attachment.
Writing \(\eta_0=1\), \(\eta_k=2\) for \(k>0\), set
\(g^{(2,\beta)}_k=f^{(2,\beta)}_k/\eta_k\) and
\(g^{(2,\beta)}_{U+1}=0\). At even levels take \(h^{(2,\beta)}_k=g^{(2,\beta)}_k\);
at odd levels take
\(h^{(2,\beta)}_k=g^{(2,\beta)}_k-g^{(2,\beta)}_{k+1}\).
The identity in
[the dual source theorem, (2)--(5)](research_mixed_next_outgoing_dual_hypergeometric_source.md)
therefore holds with \(C_{M+d,N}\) replaced by
\(C^{(2)}_{0\beta,N}(r^{M+d},W)\). Its inverse remains the complete
finite cumulative sum at odd levels. Thus neither of the two
original Fourier sectors is deleted by (15).

For real \(w\), the adopted observation estimate still applies to
every \(\mathcal O_{N,k}(w)\):
\[
|\mathcal O_{N,k}(w)|
 \le C_\epsilon e^{N\{\Gamma(1/2-k/N)+\epsilon\}},
 \qquad 0\le k\le U .
                                                                    \tag{18}
\]
Equation (18) has not acquired a new outgoing parameter. It is a
proved input for (15), rather than an estimate of its new
coefficients.

## 4. An exact endpoint feeds the new top degree

**Proposition.** For every polynomial \(f\) of degree at most \(D\),
\[
\boxed{\qquad
[W^D](\mathsf T_{0\beta}f)(W)=\frac{f(1)}{N^{1+\beta}} .
\qquad}                                                         \tag{19}
\]

To prove it, the full root product gives
\[
p_D(W)=\frac{1-W^N}{1-W}=\sum_{h=0}^D W^h,\qquad P_D=N.
                                                                    \tag{20}
\]
Only the \(j=D\) term of \(C_{\beta,N}(Z,W)\) contributes to
\([W^D]\). By (2), its coefficient is
\[
\frac1{N^{1+\beta}}\operatorname{CT}_Z
       \left[f(Z)\sum_{h=0}^D Z^{h-D}\right]
 =\frac1{N^{1+\beta}}\sum_{\ell=0}^D[Z^\ell]f(Z),
\]
which is (19). In particular even \(f=1\) produces degree exactly
\(D\). There is no vanishing numerator divided in this argument.

For the original complete conditional rows one has
\[
C_{0,N}(r^b,1)=\frac{N}{\overline{P_b}},
                     \qquad 0\le b\le D .
                                                                    \tag{21}
\]
Indeed \(C_{0,N}(1,r^b)=N/P_b\), and the exact matrix \(K\) is
Hermitian by (10)'s input. The conjugation in (21) is an algebraic
identity at a physical node; it is not inserted into the signed
transfer. Applying (19) gives
\[
\boxed{\quad
[W^D]C^{(2)}_{0\beta,N}(r^b,W)
     =\frac1{N^\beta\overline{P_b}}\ne0 .
\quad}                                                           \tag{22}
\]
Thus every physical row in (7), including \(b=D\), has output
degree exactly \(D\). Before attachment its degree was exactly
\(D-b\). The incoming support zero at \(\ell>D-b\) in (8) and
the nonzero new top output degree in (22) coexist.

For the actual Fourier coefficients, (19) says
\[
[W^D]f^{(2,\beta)}_{k,N}(W)
                     =\frac{f_{k,N}(1)}{N^{1+\beta}} .
                                                                    \tag{23}
\]
No nonvanishing of \(f_{k,N}(1)\) for every \(k\) is claimed.
There is, however, a definite nonzero case. The exact top
coefficient in the positive transition theorem, (17), is
\[
f_{U,N}(Z)=2(-q)^D\frac{S_M^2}{N^2},
\]
a nonzero constant, because only the row \(C_{D,N}=1\)
contributes. Consequently
\[
\boxed{\quad
[W^D]f^{(2,\beta)}_{U,N}(W)
                  =2(-q)^D\frac{S_M^2}{N^{3+\beta}}\ne0 .
\quad}                                                           \tag{24}
\]
The two parities give exactly
\[
[W^D]f^{(2,\beta)}_{U,N}=
\begin{cases}
4(-q)^D N^{-2-\beta},&N\text{ even},\\
8(-q)^D\cos^2(\pi/(2N))N^{-2-\beta},&N\text{ odd}.
\end{cases}                                                       \tag{25}
\]
Here \(S_M^2=2N\) at even levels. At odd levels
\(S_{(N-1)/2}^2=N\) and
\(s_M=2\cos(\pi/(2N))\), giving the second line.
The top coefficient in (24) therefore has only polynomial size.
Its monomial contribution at a specified output is that coefficient
times \(W^D\). This radial factor must remain in an estimate; the
degree increase by itself is not an exponential obstruction.

Before attachment, the exact triangular source proves
\(\deg_Z f_{k,N}\le U-k\). Equation (24) proves that this
degree assertion cannot be reused after attachment, even for
the actual largest-frequency coefficient \(k=U\).
It does not give a lower bound for the entire polynomial at a
specified complex \(W\), for its paired observation in (15), or
for the final transfer.

## 5. The precise consequence for further composition

Equations (7), (15), and (17) are a source-preserving way to use
the already proved inner Fourier bound in a subsequent attachment.
They combine the whole intermediate cycle before taking a modulus.
A later estimate may therefore work directly with this new finite
conditional source; it need not estimate every intermediate physical
value of the old remainder separately.

The outgoing action and coefficient bounds used to prove the
\(343\) gap concerned \(C_{0,N}(r^b,Z)\), not the source (7).
They do not supply a rate for (17). In particular the whole-cycle
extension cannot be justified by retaining the old degree
\(U-k\): the explicit actual coefficient (24) disproves that
shortcut. Its endpoint input \(f_{k,N}(1)\) is precisely the
source quantity in (23), not a derivative of a local geometric
packet.

There is no assertion here that this new endpoint term is too
large or fails to cancel. Nor is a hypothesis about a new action
envelope labeled as a theorem. Both
\(\mathsf T_{0\beta}E_N^-\) and the complement of the local
next attached integral also remain to be estimated in a whole
transfer proof. The algebra holds at both parities, for every
ordinary incoming color and all complex output values, and
differentiates every original ordinary jet. The analytic
reference restrictions of the adopted \(343\) theorem are
unchanged.

## Frozen source versions

- Exact torus transfer and scalar:
  8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693.
- Conditional/Fourier message bridge:
  f09dd7a3b002481eba41fefccfe5bf25c3aed87e95673f60c75e2a81fbf06e50.
- Shared-node reversal:
  53b9ac8daea4069dde59bcbe90cb991f803ef0127417c2a11081107a2b7c5843.
- Original fixed local integral:
  f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696.
- Complete \(343\) bidisk transfer:
  3baac5dfce1f55588166e519b5408f6d374a37ef6c3ca3b3b80731e73118f6fe.
- Full incoming-color observation and right source:
  5bf182877bb6905b67d68f3aafb57ec5f015b57467a9b1fb7fbff2cff2108c49.
- Positive Chebyshev transition:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Reversible odd difference and dual source:
  c4da73e92e6634940c3fd8902ad22f3e9cfa4f725e1ba73f1beeb85e3c403d6b.
- Original positive Gram identity:
  77354837ae73521349d7cc3834797c4c81dcae11f69ef1aa705223dec85ad5e8.

