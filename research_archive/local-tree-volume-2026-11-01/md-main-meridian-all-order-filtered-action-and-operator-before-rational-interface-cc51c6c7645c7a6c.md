# The filtered microscopic action and a classical characteristic of the actual operator

Private derivation, 1 November 2026. This report concerns a fixed knot for which the proved filled Conway source has its nondegenerate joint first-charge saddle and a fixed exponential gap: the long-filled strict-tree class, and the quantitative all-circle class under its stated numerical criterion. The diagram, filling powers and every compact parameter set below are fixed before the level tends to infinity.

The proposed conclusion is a source-selected classical characteristic germ for every actual all-level scalar annihilator. The argument does not identify that entire germ with the classical geometric representation curve merely because their cusp tangents agree. That further geometric identification is distinguished in Section 7.

## 1. Exact finite inputs and the new issue

Write
\[
 q_N=e^{\pi i/N},\qquad M=q_N^s,\qquad
 F_N(1)=K_N,\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{1}
\]
Here \(F_N\) is the actual zero-framed reduced ADO state in the marked coordinate \(M=-qx\). It is not the full modified-trace state. The actual latter state is \(d_N(M)F_N(M)\), with
\[
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 d_N(1)=\frac{\eta_N}{N}.
 \tag{2}
\]
All these factors remain in the argument.

The current finite source theorem, with its scalar ledger, gives a local integral or finite-contour packet whose main-parameter dependence, after the exponential errors have been removed, is exactly
\[
 A_N(s)\prod_{e\in E}\mathcal I_N(x_e,s),\qquad
 A_N(s)=\exp\!\left(\frac{\pi i\,a(D)s^2}{2N}\right),
 \quad a(D)=-w(D)-\sum_v n_v,
 \tag{3}
\]
\[
 \mathcal I_N(x,s)=
 \frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}.
 \tag{4}
\]
The single reduced-cut factor \(H_N(s)\) is outside this packet. The base packet, its phase, and its exact interpolation do not depend on \(s\). The edge set is the original physical quarter-turn set. Hidden edges introduced by an unturned binary resolution are not added to (3).

These are equations (25)–(27), (34a)–(36) of the grouped-wire packet, together with the original scalar theorem. The general component comparison supplies the discarded-source error on a fixed strict tree. The joint filling transform supplies the nonzero first joint charge and its fixed gap. For the quantitative all-circle class the explicit curvature-supported calculation supplies those same contour and gap inputs without a reciprocal-slope assumption.

The published profile on \(|s|<1\) alone is not enough to insert an arbitrary order-\(d\) operator: its equation uses \(s,s+1,\ldots,s+d\). Section 2 addresses those charts from the exact source. No principle of analytic continuation of an asymptotic expansion is substituted for that argument.

## 2. Fixed translated charts away from the resonances

Let \(K\) be a compact subset of the open upper half-plane. It may have arbitrarily large but fixed real extent. There are no ordinary or half-integer collisions on this compact set. The following checks extend the actual source bounds to \(K\), with constants depending on \(K\). They do not extend a uniform theorem across an ordinary resonance.

First, the crossing interpolation in the source-bound theorem, equation (D14), is the exact rational expression
\[
 r_{N,s}^{[n]}(z)=
 -\frac1{N(U-U^{-1})}
 \sum_{j=0}^{N-1}\lambda_j(s)^n(t_j-t_j^{-1})
              \frac{P_s(z)}{z-c_j(s)},\qquad U=e^{2\pi i s}.
 \tag{5}
\]
On \(K\), \(|U-U^{-1}|\) has a positive lower bound. The nodes remain in an ellipse of height \(O_K(N^{-1})\), and the same divided-difference estimates give a polynomial canonical norm, including its first complete normal, for every fixed positive or negative crossing power. The common full crossing scalar and mixed-order reference factors are bounded on \(K\); their exact ratios are still retained. The removable-collision maximum principle used on the unit disk is unnecessary here.

Second, Euler's product writes
\[
 W_k(s)=\prod_{\substack{1\le r\le k\\j\in\mathbb Z}}
             \left(1-\frac{s^2}{(r+jN)^2}\right),
       \qquad 0\le k<N.
 \tag{6}
\]
The indicated integers are distinct and nonzero. For \(s\in K\), the product over the finitely many small integers stays uniformly away from zero. The product of \(\min(1,|1-s^2/m^2|)\) over the remaining integers is bounded below by a positive constant, because its logarithmic tail is bounded by \(C_K\sum m^{-2}\). The corresponding product of maxima gives an upper bound. Every subset in (6) therefore has uniform upper and inverse bounds. The same is true of \(H_N(s)\), which converges uniformly to the nonzero function \(\sin(\pi s)/(\pi s)\) on \(K\).

Third, the complete-basis Newton envelopes and Hermite conditioning do not involve \(s\). Chebyshev folding depends only on the bounded number \(\cos(2\pi s)\) and the fixed raw polynomial degree divided by \(N\). The all-parity whole-trace estimates and the reflected high-index difference use finitely many polynomials \(U_{\ell-1}(\cos2\pi s)\) at each fixed-valence junction. Their bounds remain uniform on \(K\). The same old geometric pressure and strict component gaps consequently give the grouped discarded-source estimates. This does not estimate a separated return coefficient by an old tensor.

The same point applies to the local regular bare trace: its first Fourier alias has coefficient one, and every higher alias has a strict regular-window frequency gap. Replacing the unit disk by \(K\) changes only the bounded coefficients of these finitely many aliases. Its comparison to the complete bare tensor remains exponentially accurate.

Finally, use the exact translated grids in the direct crossing trace. A bounded \(s\), regardless of its real part, changes their interval endpoints by \(O_K(N^{-1})\). Use translated single-grid rectangles, retaining their endpoint currents. If a common paired rectangle is used instead, it can include or exclude a bounded number of periodic copies near the endpoints; their residues must be restored explicitly. Every such residue has angular position \(\pm\pi+O_K(N^{-1})\), so the established real-spectator endpoint bound gives the same fixed exponential loss. This point matters because the chirp is not periodic.

In particular, for the only extension needed below, \(s\mapsto s+j\) with a fixed integer \(j\), the grid is shifted by exactly \(j\) spacings and the Casimir relation is unchanged. Reindex its central \(N-|j|\) entries and retain the at most \(|j|\) wrapped entries at each endpoint. Their nonperiodic chirp factors are explicit and bounded on the fixed parameter compact; the raw Newton factor supplies the endpoint gap. Thus the local comparison is proved by finite reindexing and its retained endpoint residues, not by treating the two unwrapped grids as identical. The exact paired-grid Fourier coefficients are
\[
 (-1)^{(N-1)(\ell-1)}U_{\ell-1}(\cos2\pi\sigma),
 \qquad \sigma=s,-s,0.
 \tag{7}
\]
For the moving types on \(K\), no division by a vanishing sine occurs. The constant type is the already proved full-normal limit. The coefficient bound
\[
 |U_{\ell-1}(\cos2\pi\sigma)|
       \le \ell e^{2\pi |\operatorname{Im}\sigma|(\ell-1)}
 \tag{8}
\]
is absorbed by the same \(e^{-N\ell y}\) tails for sufficiently large \(N\). The real-spectator telescoping and the common joint angular saddle are unchanged. Fixed-power discarded errors are bounded before these angular contours, as required by the grouped-source interface.

Thus the original nonzero first-charge packet and its exact scalars hold uniformly on \(K\), with the same action and fixed exponential gaps. The threshold on the fixed filling powers, or the stated quantitative criterion, is unchanged; constants and starting levels may depend on \(K\). This extension is needed only on a finite union of small disks with positive imaginary part. It asserts no uniform result on a compact meeting a nonzero integer.

## 3. All-order canonical interpolation

The exact factorial product admits, on any fixed complex bulk compact, its expansion to every prescribed order:
\[
 \log G_N(Nx)=N J(x)+\tfrac12\log(2N\sin\pi x)
            +\sum_{j=1}^{L}N^{-j}b_j(x)+O_L(N^{-L-1}).
 \tag{9}
\]
The \(b_j\) are holomorphic and have the original logarithm marks; some of them vanish. The expansion and every fixed derivative are uniform on a smaller compact.

This follows by repeating the proof in the exact factorial interpolation note with the finite Stirling expansion to the desired order. Its remainder follows from the finite periodic-Bernoulli integral formula. In the \(k\)-th factor of the defining Gamma product, the remainder is bounded by a fixed power of \(N^{-1}\) times a summable fixed power of \(k^{-1}\). Summation therefore preserves the desired uniform order. The leading function remains the fixed primitive
\[
 J'(x)=\log(2\sin\pi x),
 \tag{10}
\]
and the half-logarithm in (9) is fixed by the exact lattice normalization. No periodic interpolation factor is introduced.

Set \(\delta=N^{-1}\), \(t=\delta s\), and define
\[
 K(x,t)=2J(x)-J(x+t)-J(x-t).
 \tag{11}
\]
Using (9) in (4), formally to any specified order, gives
\[
 \log\mathcal I_N(x,s)=
  \delta^{-1}K(x,t)+B_0(x,t)
                  +\sum_{j\ge1}\delta^j B_j(x,t).
 \tag{12}
\]
Each \(B_j\) is holomorphic near \(t=0\), even in \(t\), and vanishes at \(t=0\). In particular the \(\log N\) terms cancel. Equation (12) means a formal two-parameter construction whose substitution \(t=\delta s\) agrees with the actual fixed-\(s\) asymptotic expansion. It is not an assertion of a physical fixed-\(t\) asymptotic theorem.

The complete bare factorials, the circle Newton factors, the original integer offsets and all Gaussian amplitudes have analogous all-order bulk expansions. The finite lattice currents and the other Fourier charges have a fixed exponential loss, so they do not contribute to any coefficient of these expansions.

## 4. The filtered action theorem

Let \(X\) collect the original retained wire variables and the joint angular variables. Write \(\Phi(X)\) for the original first-charge filled phase at \(s=0\). Its critical point \(X_0\) is nondegenerate and has the original normalization. Define the analytic phase family
\[
 \Phi_t(X)=\Phi(X)+\sum_{e\in E}K(x_e,t)
                         +\frac{\pi i\,a(D)}2t^2,
 \qquad
 S(t)=\Phi_t(X_*(t)),
 \tag{13}
\]
where \(X_*(t)\) is the analytic critical point through \(X_0\). The implicit-function theorem supplies it on a fixed neighborhood of zero. This is a local analytic definition; its use does not require taking \(s=Nt\) in the physical invariant.

Formal stationary phase with the all-order analytic amplitude of Section 3 gives
\[
 \log\frac{F_N(q_N^s)}{K_N H_N(s)}
 \sim N\{S(t)-S(0)\}
             +\sum_{j\ge0}N^{-j}\{C_j(t)-C_j(0)\},
 \qquad t=s/N.
 \tag{14}
\]
Here the \(C_j\) are holomorphic germs. The leading amplitude is nonzero, so its logarithm is fixed by the ratio at \(t=0\). Possible residue-class dependence of lower amplitudes can be treated separately; the phase \(S\) is the same. The original powers of \(N\) and the scalar independent of \(s\) cancel in the displayed ratio.

For an explicit justification, perform formal Gaussian expansion of the local phase \(\Phi_t\), uniformly for small \(t\). Every coefficient is a finite polynomial in derivatives of the phase and amplitude and in the inverse Hessian. These derivatives are holomorphic in \(t\), and the Hessian stays invertible. Substitute \(t=\delta s\), Taylor-expand the resulting analytic coefficient functions, and truncate at any chosen power of \(\delta\). The uniform contour remainder and the exponentially small discarded terms prove the same fixed-\(s\) asymptotic coefficient. This argument applies on the original disk and on the translated compacts of Section 2.

Consequently, writing the logarithm as
\[
 \log\frac{F_N(q_N^s)}{K_N H_N(s)}
       \sim\sum_{r\ge1}N^{-r}p_r(s),
 \tag{15}
\]
each \(p_r\) is a polynomial of degree at most \(r+1\). More precisely, its coefficient of \(s^{r+1}\) is exactly the coefficient of \(t^{r+1}\) in \(S(t)-S(0)\). Terms from the \(C_j\) have degree at most \(r\) and cannot contribute to this top diagonal. This proves the filtration, rather than inferring it from a few low-order coefficients.

The phase is even in \(t\). At its base critical point the first mixed derivatives in \(X,t\) vanish, so
\[
 S'(0)=0,\qquad
 S''(0)=-2\pi\sum_e\cot(\pi x_e^{\mathrm{fill}})
                                      +\pi i\,a(D)
        =\pi i\,\tau_K.
 \tag{16}
\]
The last equality uses the independently proved preferred-cusp formula. Higher derivatives of \(S\) are fixed by (13), not by the cusp tangent alone.

## 5. Exact operator compatibility on the shifted charts

Let
\[
 P(q,M,T)=\sum_{j=0}^{d}a_j(q,M)T^j,\qquad TM=qMT,
 \tag{17}
\]
be any specified nonzero actual all-level reduced-state annihilator. Clear its fixed rational denominators and remove its common \(q-1\) valuation. Denote its first nonzero classical symbol by \(P_0(M,L)\). No geometric factor is appended.

The exact reduced/full ratio in (2) satisfies
\[
 \frac{d_N(q_N^jM)}{d_N(M)}
    =(-1)^j\frac{q_N^jM-q_N^{-j}M^{-1}}{M-M^{-1}}.
 \tag{18}
\]
Thus, with \(f(M)=M-M^{-1}\), the same normalized function on the left of (15) obeys the actual root equation obtained from
\[
 \widetilde P
  =\sum_{j=0}^{d}a_j(q,M)(-1)^j
                      \frac{f(M)}{f(q^jM)}T^j.
 \tag{19}
\]
This is a fixed rational Ore operator. It retains the meridian divisor and sign character. Multiplying it on the left by \(\prod_{j=1}^{d}f(q^jM)\) clears its additional denominators. Its first classical symbol is
\[
                  f(M)^d P_0(M,-L).
 \tag{20}
\]
The displayed meridian factor is recorded, not removed by a normalization convention.

Choose a small open disk \(D\) in the upper half-plane and put \(K=\bigcup_{j=0}^{d}(\overline D+j)\). Section 2 supplies the same all-order expansion at every argument in this exact equation. Division by the nonzero normalized state at \(s\in D\) and comparison of every asymptotic coefficient therefore gives its formal difference equation. All coefficient functions vanish on \(D\), hence identically as their polynomial or meromorphic functions of \(s\).

This is the required compatibility step. Exact ordinary-color values alone would not have supplied these shifted neighborhoods, and a formal expansion restricted to \(|s|<1\) would not have justified it for arbitrary operator order.

## 6. Diagonal extraction forces a classical characteristic germ

Now write \(h=\log q\), \(u=\log M\), so \(u=hs\), and put
\[
 \mathcal S(u)=\pi i\{S(u/(\pi i))-S(0)\}.
 \tag{21}
\]
The degree filtration in Section 4 regrades the formal logarithm uniquely as
\[
             h^{-1}\mathcal S(u)+\sum_{j\ge0}h^j A_j(u).
 \tag{22}
\]
Indeed a monomial \(h^rs^k\) becomes \(h^{r-k}u^k\), and \(k\le r+1\) permits only the single negative power \(h^{-1}\). For each exponent of \(h\), its coefficient is a formal series in \(u\).

Under the \(j\)-fold shift \(s\mapsto s+j\), the ratio of these formal periods belongs to \(\mathbb C[[h,u]]\), with constant \(h\)-coefficient
\[
                           e^{j\mathcal S'(u)}.
 \tag{23}
\]
The \(h^{-1}\) cancels in the finite difference \(\mathcal S(u+jh)-\mathcal S(u)\). All the \(A_j\) contribute zero to the constant coefficient of that difference.

The substitution \(\mathbb C[[h,u]]\to\mathbb C[s][[h]]\), \(u\mapsto hs\), is injective: distinct monomials \(h^au^b\) yield the distinct monomials \(h^{a+b}s^b\). Consequently the formal compatibility from Section 5 is an identity before this substitution. Taking its constant \(h\)-coefficient and using (20) gives
\[
 f(e^u)^d\,P_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{24}
\]
The first factor is a nonzero formal series. The formal series ring is a domain, so
\[
                  P_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{25}
\]
This deduction retains the factor in the operator and cancels it only in a domain identity. It does not silently discard a peripheral component.

The analytic germ
\[
                    M=e^u,\qquad L=-e^{\mathcal S'(u)}
 \tag{26}
\]
therefore lies on the first nonzero classical symbol of every actual all-level annihilator. Its \(M\) coordinate is nonconstant, so the kernel of the map from the Laurent polynomial ring in \(M,L\) to this analytic germ is a height-one prime. It is generated by an irreducible Laurent polynomial, and that polynomial divides every such \(P_0\). The marked reduced sign is \(L(0)=-1\), and
\[
             \left.\frac{d\log(-L)}{du}\right|_{u=0}
                 =\mathcal S''(0)=\tau_K.
 \tag{27}
\]
This is an actual source-selected characteristic, derived from the given operator and its selected microscopic family. A nonminimal left multiple does not create a choice in (26): the phase was fixed by the physical source, and (25) also applies to a minimal annihilator if one is specified.

## 7. Exact remaining geometric identification and limitations

Equations (13), (21), and (26) construct a complete analytic germ, not just its first cusp jet. The proof above does not yet establish that this germ is the marked preferred-longitude eigenvalue of a nonparabolic representation of the filled knot group. The published Conway face family keeps the main cusp parabolic; its preferred-cusp calculation proves (16), not that additional nonparabolic identification.

A sufficient next step is an exact classical adapter: identify the stationary equations of (13), with \(t=u/(\pi i)\), with the original regular geometric critical scheme of the full marked braid source, retaining its cut flag, framing and preferred longitude insertion. The existing marked braid holonomy theorem identifies that latter scheme with framed knot representations and supplies its rational inverse. An identification of these equations on the complete geometric germ would therefore identify (26) with the geometric eigenvalue germ and prove the desired geometric factor by (25). Agreement of their tangent alone is not sufficient.

The argument also does not claim a physical asymptotic formula for fixed \(M\ne1\), or for \(s\) growing with \(N\). The variable \(t\) in Section 4 is an auxiliary analytic parameter used to organize all fixed-\(s\) coefficients. The ordinary-color divisors remain in (2), (18)–(20). The translated charts in Section 2 stay away from those divisors; no uniform nonvanishing state across ordinary-color resonances has been asserted.

The translated-chart extension and its use of the general component error estimates should be checked against the complete source proof before this report is treated as a new theorem. The algebraic filtration and diagonal extraction are independent of that source audit once its stated hypotheses hold.
