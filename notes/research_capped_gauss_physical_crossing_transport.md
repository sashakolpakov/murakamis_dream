# Whole-meridian transport of the capped Gauss row through a physical crossing

Private written proof, 23 November 2026.

The actual terminal Gauss row times one positive physical crossing
is exactly a reflected copy of the whole meridian row with an explicit
clock multiplier. This identity retains every coordinate and normal
tail. It gives a scalar-relative, nonzero transport theorem for the
original capped initializer at \(M=\exp(v/\sqrt N)\), without applying
a large crossing matrix to an asymptotic approximation.

The result concerns one physical generator. No closure under arbitrary
signed words, original turns, or an exterior marked closing is asserted.

## 1. Actual matrices, with the full crossing scalar

Keep the fixed root and the actual balanced meridian family:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 M\ne0,\quad x=-M/q,\quad F_j=(Q;Q)_j,\quad
 g_j(M)=(M^{-2}Q;Q)_j .
 \tag{CT1}
\]
On a physical degree \(0\le T\le d\), write
\[
 C=Q^{-T-1},\quad K_T=M^2C,\quad
 H_d=(-1)^dM^dg_d,\quad
 A(M)=q_F(M)E_\Sigma(M)^di_d,\quad r(M)=e_T^{\mathsf T}A(M).
 \tag{CT2}
\]
The restriction to degree \(T\) is understood. The source \(A\) is the
actual capped Gauss operator of G489 and (MC1), with the original
ordered coproduct. Its lowering coefficient is
\(E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\), with bottom zero.

Let \(R_{\rm full}(M)\) be the actual positive checked crossing on
these two equally colored heads. Use its original unrolled logarithm:
\[
 \alpha(M)=d+\frac{N}{\pi i}\Log M,\qquad
 \varkappa(M)=q^{\alpha(M)^2/2},\qquad
 B(M)=\varkappa(M)^{-1}R_{\rm full}(M).
 \tag{CT3}
\]
The branch is continued from \(M=1\). All displayed \(q\)-powers
mean their indicated exponentials. The stripped matrix \(B\) is
Laurent polynomial in \(M\); the full scalar remains in (CT3).

For input \((a,b)\), output \((b+h,a-h)\), and
\(0\le h\le\min(a,d-b)\), its complete coefficient is
\[
 B_{b+h,a-h;\,a,b}
 =x^{-a-b-h}M^{2h}Q^{ab-(b+1)h}
       \frac{g_a(M)}{g_{a-h}(M)}
       \frac{F_{b+h}}{F_bF_h}.
 \tag{CT4}
\]
The quotient \(g_a/g_{a-h}\) is the finite interval product, so
this formula has no meridian poles.
To check the generic family, the original preflip factorization is
\(D P_N(e_xf)\), with the full Cartan
\(D=q^{\mathsf h_\alpha\otimes\mathsf h_\alpha/2}\).
The actual \(h\)-fold lowering coefficient is
\(x^{-h}(M^2Q^{-a};Q)_h\).
Reflection of its factors gives
\[
 (M^2Q^{-a};Q)_h
 =(-1)^hM^{2h}Q^{-ah+h(h-1)/2}\,g_a/g_{a-h}.
 \]
Combining this with the finite Euler coefficient
\((-1)^hQ^{h(h-1)/2}/F_h\), the raising coefficient
\(F_{b+h}/F_b\), and the Cartan ratio
\(x^{-a-b}Q^{(a-h)(b+h)}\), proves (CT4).
Thus no complete-only coefficient has been differentiated.

## 2. An exact row reflection, before any asymptotic

The whole terminal row formula (MC6), with \(k_a=T-a\), is
\[
 r_a(M)=H_dK_T^d x^{-k_a}M^{-2k_a}Q^{Tk_a}
       \frac{F_T}{g_T}
       \frac{g_{k_a}}{F_{k_a}}
       \frac{(M^{-4}Q^{T+1};Q)_a}{F_a}.
 \tag{CT5}
\]
Its proved finite summation has length at most \(T<N\) and does
not require the upper-chamber restriction. Apparent denominators
are first interpreted near \(M=1\); the cleared entries are Laurent
polynomials, as in (MC7).

The exact transport identity, for every \(0\le j\le T\), is
\[
 \boxed{\qquad
 (r(M)B(M))_j=x^{-T}(M^4C)^j r_{T-j}(M).
 \qquad}
 \tag{CT6}
\]
Here both rows have all \(T+1\) physical coordinates.
We give the entire finite cancellation. Put \(P=M^{-4}Q^{T+1}\)
and \(J_0=H_dK_T^dF_T/g_T\). The contribution of output row
coordinate \(T-b\) and input first occupation \(j\) has transfer
\(h=j-b\), with \(0\le b\le j\). Substitution of (CT4)--(CT5)
cancels \(g_b\) and \(F_{T-b}\), leaving
\[
 \begin{split}
 (rB)_j={}&J_0x^{-T-j}M^{2j}Q^{-j}
                      \frac{g_j}{F_{T-j}}\\
 &{}\times\sum_{b=0}^j
 \frac{M^{-4b}Q^{(2T-j+1)b}(P;Q)_{T-b}}
                         {F_bF_{j-b}} .
 \end{split}
 \tag{CT7}
\]
Set \(D=P Q^{T-j}\). The last sum is
\[
 \frac{(P;Q)_{T-j}}{F_j}
       \sum_{n=0}^j{j\brack n}_Q D^{j-n}(D;Q)_n
             =\frac{(P;Q)_{T-j}}{F_j}.
 \tag{CT8}
\]
For an elementary proof of the equality to one, apply Gaussian Pascal
\({j+1\brack n}={j\brack n-1}+Q^n{j\brack n}\).
The two sums combine, term by term, through
\((D;Q)_{n+1}+DQ^n(D;Q)_n=(D;Q)_n\).
Induction starts at \(j=0\). Only factorials with index below \(N\)
occur.

Finally \(M^2/(Qx)=x\), so (CT7) becomes
\[
 (rB)_j=J_0x^{j-T}
           \frac{g_j(P;Q)_{T-j}}{F_jF_{T-j}}.
 \tag{CT9}
\]
Comparison with (CT5) at \(T-j\), using
\(C=Q^{-T-1}\) and \(Qx^2=M^2\), proves (CT6).
The proof is on a generic neighborhood only to allow the displayed
ratios; Laurent continuation proves every exceptional meridian value.
In particular the nonzero first-normal tail is transported, not
omitted using the root support.

As a quantitative whole-row consequence in the original flat
occupation norm,
\[
 \begin{split}
 \min(|M|^{-T},|M|^{3T})\|r(M)\|_2
 &\le\|r(M)B(M)\|_2\\
 &\le\max(|M|^{-T},|M|^{3T})\|r(M)\|_2 .
 \end{split}
 \tag{CT10}
\]
This is just the exact diagonal modulus in (CT6), followed by
reflection. At \(|M|=1\) it is equality.
For \(M=e^{v/\sqrt N}\), \(|v|\le V\), the two comparison
factors lie between \(e^{-3V\sqrt N}\) and \(e^{3V\sqrt N}\).
For the full physical crossing both sides retain the multiplier
\(|\varkappa(M)|\). No claim about the crossing on arbitrary rows
is inferred from (CT10).

## 3. Exact transport with the original cap

Now impose the upper-chamber conditions of PC405:
\[
 \ell=d-T\ge1,\quad t=N-2\ell>0,\quad
 \alpha_N=\ell/N\in I\Subset(0,1/2),\quad
 a_*=\lfloor\ell/2\rfloor,\quad k=t-1=T-\ell.
 \tag{CT11}
\]
Keep exactly the root-frozen \(D,F_c\), original \(c_T(z)\),
period \(\mathscr S_N\), central entry \(f_N(u)\), and constants
\(V_\alpha,H_\alpha,\kappa_\alpha\) of (PC2)--(PC3).
Thus \(D_{aa}=q^{\ell a}\) and
\(\beta_b=\binom db\binom d{T-b}\).
The different symbols \(\varkappa\) and \(\kappa_\alpha\) mean,
respectively, the physical crossing scalar and the Gaussian tilt.
Define the actual stripped crossed period
\[
 \mathscr S_N^+(u,z)
   =e_T^{\mathsf T}\bar D A(M)B(M)\bar D F_c c_T(z),
       \qquad M=e^{u/N}.
 \tag{CT12}
\]
For bookkeeping only, let \(\mathscr S_N^{[w]}(u,z)\) mean the
same uncrossed period with the additional diagonal \(w^a\)
between \(A(M)\) and the following \(\bar D\).
This diagonal is not a new closing functional.

The finite row identity gives the cap-preserving identity
\[
 \boxed{\quad
 \mathscr S_N^+(u,z)
 =D_{TT}x^{-T}M^{4T}z^T
          \mathscr S_N^{[M^{-4}]}(u,z^{-1}).
 \quad}
 \tag{CT13}
\]
This is first an identity for \(z\ne0\), and is polynomial after
clearing the displayed inverse argument.
Indeed \(D_{T-a,T-a}=D_{TT}\bar D_{aa}\),
\((F_c)_{T-a,b}=(F_c)_{a,T-b}\), and
\(\beta_{T-b}=\beta_b\). Reindex \(j=T-a\) in (CT6), then
\(b\mapsto T-b\) in the actual cap, to obtain (CT13).
Every Fourier phase and the whole binomial cap have been retained.

The natural central crossed normalizer is itself a literal entry ratio:
\[
 f_N^+(u)
 :=\frac{(r(M)B(M))_{T-a_*}}
            {(r(1)B(1))_{T-a_*}}
       =M^{3T-4a_*}f_N(u).
 \tag{CT14}
\]
Its denominator is nonzero by (PC5)--(CT6).
For the full crossing, replace \(f_N^+\) by
\(\varkappa(M)f_N^+/\varkappa(1)\).

## 4. A relative asymptotic through the actual generator

For every fixed complex disks \(|v|\le V\), \(|\zeta|\le Z\),
with \(V,Z>0\) independent of \(N\), put
\(z_N^+(\zeta)=q^{-k}e^{\zeta/\sqrt N}\). Then
\[
 \boxed{\quad
 \frac{\mathscr S_N^+(\sqrt N\,v,z_N^+(\zeta))}
      {f_N^+(\sqrt N\,v)\,
                     \mathscr S_N^+(0,z_N^+(\zeta))}
 =\exp\left\{
       \frac{\bar\kappa_{\alpha_N}^{\,2}v^2}{4H_{\alpha_N}}
       +\frac{i\pi V_{\alpha_N}\bar\kappa_{\alpha_N}v\zeta}
                    {H_{\alpha_N}}\right\}
                    +o_{I,V,Z}(1).
 \quad}
 \tag{CT15}
\]
The bar conjugates the constant \(\kappa_\alpha\), not \(v\) or
\(\zeta\). Quotients at ordinary zeros are interpreted removably.
The statement and its holomorphic derivatives are uniform on
smaller fixed disks. In original meridian \(\mu=v/\sqrt N\),
order \(j\) differentiation retains the factor \(N^{j/2}\).

Here is why this follows from the actual estimates in PC405,
rather than an unproved stability of a remainder under \(B\).
In (CT13), \(z^{-1}=q^ke^{-\zeta/\sqrt N}\).
After extraction of \(M^{-4a_*}\), the extra diagonal contributes
\[
 M^{-4(a-a_*)}
   =\exp\{-4v(a-a_*)/\sqrt N\}.
 \tag{CT16}
\]
On the central occupation scale
\(y=(a-\ell/2)/\sqrt N\), its limit is \(e^{-4vy}\).
Thus the head Gaussian integral (PC20) has tilt
\(\kappa_\alpha-4\) and cap variable \(-\zeta\).
Its domination remains a Gaussian times \(e^{C_V|y|}\).
For off-central coordinates, (CT16) costs at most \(e^{C_V\sqrt N}\);
this is absorbed by the same
\(e^{-c_IN+C_V\sqrt N\log(N+1)}\) estimates as in PC405.
The true \(a>\ell\) tail obeys exactly the same conclusion.
All shared ordinary zeros and the maximum-principle removal from
(PC17)--(PC19) remain valid after a nonzero diagonal multiplier.

Consequently the divided auxiliary period has relative limit
\[
 \exp\left\{\frac{(\kappa_\alpha-4)^2v^2}{4H_\alpha}
       -\frac{i\pi V_\alpha(\kappa_\alpha-4)v\zeta}{H_\alpha}\right\}.
 \tag{CT17}
\]
In (CT13) the remaining meridian monomial, relative to its root
value, is \(M^{-T+4T-4a_*}=M^{3T-4a_*}\), exactly (CT14).
Finally \(\operatorname{Re}\kappa_\alpha=2\), so
\(\kappa_\alpha-4=-\bar\kappa_\alpha\).
This proves (CT15), including every scalar in (CT13).

At the root, (CT13) reduces to
\[
 \mathscr S_N^+(0,z)
   =D_{TT}x_0^{-T}z^T\mathscr S_N(0,z^{-1}),
 \tag{CT18}
\]
which is nonzero on the stated activity collar for large \(N\)
by PC405. The right side of (CT15) is also nonzero on every
fixed compact parameter set. Hence the divided crossed period
is a holomorphic unit there for large \(N\). Its only meridian
zeros are the same simple ordinary zeros
\(v=i\pi j/\sqrt N\ne0\); their divided normals are retained.
All fixed scaled jets follow by Cauchy from slightly larger disks.

For the full physical period, multiply (CT12) by
\(\varkappa(M)\), and use the full normalizer following (CT14).
Explicitly, on the retained logarithm,
\[
 \frac{\varkappa(e^{u/N})}{\varkappa(1)}
       =\exp\left\{\frac{du}{N}+\frac{u^2}{2\pi iN}\right\}.
 \tag{CT19}
\]
This factor is not replaced by a unit-modulus bound. Other external
framing or meridian factors remain in their original positions and
their own derivatives are not included in (CT15).

The advance is an exact whole-family physical crossing step and
its scalar-relative capped estimate. An inverse crossing from the
resulting family can of course undo the same exact step; this does
not assert closure for arbitrary successive signs or native turns.
Such compositions must still transport the full graded kernel,
the complement, and the actual exterior covector.
No filled-knot or arbitrary-short-component lower bound follows here.

## Complete proof inputs and coverage

The adopted PC405 was freshly read whole, at SHA256
81cf79171ed28c3a5cdd6da93de78bebad83d82049a27b9cafecb3798bf150d3:
notes/research_capped_gauss_parabolic_meridian_collar.md.
The complete adopted MC430 and its source conventions were retained
whole at the current ledger pin
b7ba8e8229e4317029df825660b25466ede91f3f274756dd836610f09e91cb30.
All nine original proof texts and their complete comparison texts
listed in PC405 remain whole/current at their renewed matching pins.

The complete actual crossing inputs are
notes/actual_shared_quantum_flags_and_charged_exchange.md (459 lines),
dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9,
and notes/research_real_meridian_krein_transport.md (310 lines),
caf18090cb75a0527ffccdf4a3217fe422876d683271eda8e3e6d591259e92dc.
The full unrolled Cartan and generic meridian coefficients used in
(CT3)--(CT4) are precisely those of the latter's (2),(6).

Complete comparison coverage was checked:
notes/research_gauss_physical_crossing_factorization.md (383 lines),
54d1b6c1e200cab6ca6e5affc49c98fe57d7c395a542d5f8afe502345884486f,
proves an operator identity at the root and explicitly retains its
uncomputed meridian defect. The present result evaluates a terminal
row on the whole meridian family; it is not an extension of that
whole-operator equality. The whole meridian-frame506,
6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976,
was also checked; its exact diagonal crossing gauges do not give the
capped scalar-relative result (CT15).
No mathematical program, test, build or git operation was used.
