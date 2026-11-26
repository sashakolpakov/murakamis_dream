# A common radial dual for the actual reduced first-meridian-jet source

Private written proof, 19 November 2026.

Both Cartan insertions in the original reduced source can be moved to
scalar weights on one and the same capped projective angular period.
The whole meridian formula has an explicit simple polar dual. Its
integrated residue is zero by the actual pointed-source identity;
subtracting that specified residue gives a pointwise holomorphic
integrand on a meridian collar of radius proportional to \(N^{-1}\).
The resulting first-normal weight has only real radial zeros. It is
therefore a uniform unit near a nonreal geometric total moment.

This is a statement about the exact closing coupon, not nonvanishing
of its angular period. No geometric relative-cycle coefficient is
inferred. The complete directs are R and P, pinned at the end.

## 1. One actual angular polynomial

Fix \(N\ge5\), \(m\ge2\), and put
\[
 d=N-1,\quad r=m-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad x_0=-q^{-1},\quad \varepsilon=(-1)^{(N+1)r}.
 \tag{1}
\]
The common meridian is \(M=e^\mu\); \(q=q_N\) is fixed when
differentiating. Let \(W(M)\) be an actual finite braid word, with
its prescribed scalar and zero-framing factors, and let

\[
 B(M)=\mathcal B_m(W(M)),\qquad
 T(M)=\mathcal G^{-1}B(M)\mathcal G
       =T_L(M)\cdots T_1(M) .
 \tag{2}
\]
Here \(\mathcal B_m\) is R's literal prefix quotient and
\(\mathcal G=G_F^{\otimes r}\), \(G_Fw_a=(Q;Q)_aw_a\), is P's
meridian-independent factorial gauge. Take \(L\ge1\), inserting
an identity for the empty word. R proves that its generators are
the physical crossings on the remaining heads and the explicit
Euler star \(\kappa S_rD_{\rm red}\), with their actual inverses.
All these factors preserve exact integer total occupation, throughout
the meridian family.

For \(0\le k\le rd\), retain the original capped block
\[
 I_k=\{a\in\{0,\ldots,d\}^{r}:|a|=k\},\qquad
 V_k=\operatorname{span}\{w_a:a\in I_k\},\qquad
 (r)_k=\frac{(k+r-1)!}{(r-1)!}.
 \tag{3}
\]
For a matrix \(A\) on \(V_k\), P's exact kernel is
\[
 \mathscr K_{A,k}(\zeta,\eta)
       =(r)_k\sum_{a,b\in I_k}\zeta^a A_{ab}\frac{\eta^b}{b!}.
 \tag{4}
\]
Let \(d\nu\) be the probability projective measure obtained from
the unit sphere in \(\mathbb C^r\). The closed product
\[
 F_k(M;\boldsymbol\zeta)=
 \mathscr K_{T_{L,k},k}(\zeta_0,\overline\zeta_{L-1})\cdots
 \mathscr K_{T_{1,k},k}(\zeta_1,\overline\zeta_0)
 \tag{5}
\]
is invariant under each choice of unit representative of its
projective arguments. For \(L=1\) use the single diagonal kernel.
The exact sphere moments give
\[
 \int_{(\mathbb P^{r-1})^L}F_k(M;\boldsymbol\zeta)\,d\nu^L
       =t_k(M):=\operatorname{Tr}_{V_k}T(M).
 \tag{6}
\]
For \(r=1\), projective space is a point. No state outside \(I_k\)
is present, even when \(k>d\).

Define the unrotated radial polynomial
\[
 \mathcal P_N(s,\mu;\boldsymbol\zeta)
     =\sum_{k=0}^{rd}\frac{(Ns)^k}{(r)_k}
                            F_k(e^\mu;\boldsymbol\zeta),
 \qquad
 d\gamma_{r,N}(s)=\frac{N^r}{(r-1)!}e^{-Ns}s^{r-1}\,ds.
 \tag{7}
\]
The radial measure initially has the path \(s\in[0,\infty)\).
The polynomial has degree at most \(rd\), and all its coefficients
are analytic in \(\mu\) and smooth on the compact projective product.
The gamma moment is exactly
\[
       \int_0^\infty\frac{(Ns)^k}{(r)_k}\,d\gamma_{r,N}(s)=1.
 \tag{8}
\]
Thus the same polynomial, rather than two separately chosen angular
kernels, will occur in both Cartan terms below.

## 2. Moving both Cartan rotations to the radial dual

Put \(\chi_k=x_0^rQ^{-k}\). P's two exact trace integrals are
\[
 \mathcal I_\pm(\mu)=
 \int_0^\infty d\gamma_{r,N}(s)\int d\nu^L\,
                   \mathcal P_N(Q^{\mp1}s,\mu;\boldsymbol\zeta),
 \qquad
 \operatorname{Tr}(K_0^{\pm1}B(e^\mu))
                         =x_0^{\pm r}\mathcal I_\pm(\mu).
 \tag{9}
\]
In the plus integral make the exact substitution \(t=Q^{-1}s\).
The measure contributes \(Q^r\), and its exponential becomes
\(e^{-NQt}\). The new path is \(Q^{-1}[0,\infty)\). It can be
rotated back to the positive ray without crossing a singularity.
Indeed on the intervening sector \( -2\pi/N\le\arg t\le0\),
\[
                       \Re(Qt)\ge |t|\cos(2\pi/N)>0.
 \tag{10}
\]
At fixed \(N\) the other factor is a polynomial of degree at most
\(rd+r-1\). The integral over a closing arc of radius R is bounded
by a constant times
\(R^{rd+r}e^{-N R\cos(2\pi/N)}\), which tends to zero. On a
compact meridian set its coefficient bound is uniform, also after
any fixed derivative. At zero the density is holomorphic and the
small arc vanishes. These estimates are uniform in the projective
variables because that domain is compact. The same proof for the
minus integral uses \(t=Qs\) and \(e^{-NQ^{-1}t}\).

Consequently, exactly,
\[
 \mathcal I_\pm(\mu)=Q^{\pm r}
 \int_0^\infty d\gamma_{r,N}(s)\int d\nu^L\,
 e^{-N(Q^{\pm1}-1)s}\mathcal P_N(s,\mu;\boldsymbol\zeta).
 \tag{11}
\]
No infinite exponential kernel or occupation interpolation was used.
The restriction \(N\ge5\) ensures the strict decay in (10).

Set
\[
 \begin{split}
 A_N(s)&=x_0^{-r}e^{-N(Q-1)s},\\
 B_N(s)&=x_0^{r}e^{-N(Q^{-1}-1)s}.
 \end{split}
 \tag{12}
\]
Here \(x_0^rQ^r=x_0^{-r}\) and its inverse identity account for
the apparently reversed prefactors. Equations (9)--(11) prove
\[
 \operatorname{Tr}(K_0B(e^\mu))=\int A_N\mathcal P_N\,d\gamma\,d\nu^L,
 \qquad
 \operatorname{Tr}(K_0^{-1}B(e^\mu))=\int B_N\mathcal P_N\,d\gamma\,d\nu^L.
 \tag{13}
\]

## 3. The whole meridian source and its specified residue

The original pointed source, without any separately prescribed
outside scalar, is
\[
 \Phi_N(\mu)=\operatorname{Tr}_{\rm full}
             ((P_0\otimes K_{\rm r}(e^\mu)^{1-N})W(e^\mu)).
 \tag{14}
\]
It is analytic at zero. R's exact meromorphic source identity is
\[
 \Phi_N(\mu)=\operatorname{Tr}_{\rm r}
 \left(\frac{D_N(e^\mu)}{D_N(e^\mu K_{\rm r}(e^\mu))}B(e^\mu)\right),
 \qquad D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{15}
\]
The Laurent-polynomial continuation defines \(D_N\) at \(z=\pm1\).
Since \(K_{\rm r}(e^\mu)=e^{r\mu}K_0\) and
\(\chi_k^N=\varepsilon\), its generic scalar weight on \(V_k\) is
\[
 \frac{D_N(e^\mu)
           (e^{m\mu}\chi_k-e^{-m\mu}\chi_k^{-1})}
                 {\varepsilon(e^{mN\mu}-e^{-mN\mu})}.
 \tag{16}
\]
All removable self-Cartan cases are interpreted by this whole
identity, not by separate substitutions into its numerator.
Combining (13) and (16) gives the exact common-angular formula
\[
 \boxed{\displaystyle
 \Phi_N(\mu)=\int_0^\infty d\gamma_{r,N}(s)\int d\nu^L\,
                \mathcal W_N(s,\mu)\mathcal P_N(s,\mu;\boldsymbol\zeta),
 \quad
 \mathcal W_N(s,\mu)=
 \frac{D_N(e^\mu)
              (e^{m\mu}A_N(s)-e^{-m\mu}B_N(s))}
                  {2\varepsilon\sinh(mN\mu)}.}
 \tag{17}
\]
This is first an equality away from its meridian poles and then
an equality with the original analytic continuation.

For its root expansion define
\[
 \mathfrak c_N(s)=\frac{A_N(s)+B_N(s)}{2\varepsilon},\qquad
 \mathfrak d_N(s)=\frac{A_N(s)-B_N(s)}{2\varepsilon m}.
 \tag{18}
\]
The function \(D_N(e^\mu)=\sinh(N\mu)/\sinh\mu\) is even and
has value N at zero. Expansion of (17) therefore gives
\[
       \mathcal W_N(s,\mu)
               =\frac{\mathfrak d_N(s)}\mu+\mathfrak c_N(s)+O(\mu).
 \tag{19}
\]
Finite polynomial coefficients and the decay proved in Section2
justify integration of this Laurent expansion. Analyticity of the
actual left side in (14) proves the precise residue identity
\[
            \int d\gamma\,d\nu^L\,
                    \mathfrak d_N(s)\mathcal P_N(s,0;\boldsymbol\zeta)=0.
 \tag{20}
\]
This is also P's original Cartan residue row. It is an integrated
identity, not pointwise vanishing on the angular domain.

Fix \(0<c<\pi/m\). On the shrinking collar
\(|\mu|<c/N\), the only zero of \(\sinh(mN\mu)\) is zero.
The explicitly regularized integrand
\[
 \mathcal R_N(s,\mu;\boldsymbol\zeta)=
 \mathcal W_N(s,\mu)\mathcal P_N(s,\mu;\boldsymbol\zeta)
       -\frac{\mathfrak d_N(s)}\mu
                              \mathcal P_N(s,0;\boldsymbol\zeta)
 \tag{21}
\]
is pointwise holomorphic in \(\mu\) there, including at zero.
Equation (20) shows that its integral is still exactly \(\Phi_N\).
No fixed meridian disk independent of N is asserted: other zeros
of the displayed hyperbolic sine approach zero at scale \(N^{-1}\).
The actual word and any outside scalar must retain their own domains.

Taking the value at zero yields the complete first-jet pairing
\[
 \boxed{\displaystyle
 \Phi_N(0)=\int d\gamma\,d\nu^L\,
 \left\{\mathfrak c_N(s)\mathcal P_N(s,0;\boldsymbol\zeta)
       +\mathfrak d_N(s)\partial_\mu
                              \mathcal P_N(s,0;\boldsymbol\zeta)\right\}.}
 \tag{22}
\]
At \(M=1\), \(\partial_\mu=\partial_M\). This derivative acts on
the entire actual reduced product, including all local scalars and
moving matrices. The frozen complete Cartan has not been
differentiated again. Its required meridian factors are already
the \(e^{\pm m\mu}\) in (17).

## 4. A uniform nonzero first-normal coupon off the real radial axis

Put
\[
 \vartheta_N=2\pi/N,\qquad
 \eta_N(s)=N\sin\vartheta_N\,s-r\vartheta_N/2,\qquad
 \mathcal E_N(s)=(-1)^r e^{N(1-\cos\vartheta_N)s}.
 \tag{23}
\]
Direct collection of the root phases in (12) gives
\[
 A_N=\mathcal E_Ne^{-i\eta_N},\qquad
 B_N=\mathcal E_Ne^{i\eta_N},\qquad
 \mathfrak c_N=\frac{\mathcal E_N}\varepsilon\cos\eta_N,
 \quad
 \mathfrak d_N=-\frac{i\mathcal E_N}{\varepsilon m}\sin\eta_N.
 \tag{24}
\]
In particular the whole dual is
\[
 \mathcal W_N(s,\mu)=
 \frac{D_N(e^\mu)\mathcal E_N(s)
                       \sinh(m\mu-i\eta_N(s))}
                    {\varepsilon\sinh(mN\mu)}.
 \tag{25}
\]
Every zero of \(\mathfrak d_N\) is real, namely
\[
          s=\frac{\pi j+\pi r/N}{N\sin(2\pi/N)},
                         \qquad j\in\mathbb Z.
 \tag{26}
\]
This is a finite-source statement, not evaluation of a classical
Cartan symbol at a nonphysical occupation.

More quantitatively let K be a fixed compact subset of
\(\mathbb C\setminus\mathbb R\), with
\(|\Im s|\ge\delta>0\) and \(|\Re s|\le R\) there. Since
\[
 |\sin(x+iy)|^2=\sin^2x+\sinh^2y,
 \quad
 N\sin(2\pi/N)\ge5\sin(2\pi/5)>0,
 \quad
 N(1-\cos(2\pi/N))\le2\pi^2/5,
 \]
equation (24) gives the uniform positive lower bound
\[
 |\mathfrak d_N(s)|\ge
 \frac{e^{-2\pi^2R/5}}m
        \sinh\bigl(5\sin(2\pi/5)\,\delta\bigr)>0.
 \tag{27}
\]
The sine bound follows from concavity of sine on
\([0,2\pi/5]\); the cosine bound follows from
\(1-\cos t\le t^2/2\). Upper bounds and all fixed holomorphic
derivatives of this weight and its reciprocal are uniform on
smaller compact buffers off the real axis. Indeed their exponential
and trigonometric coefficients are bounded, and (27) permits
Cauchy estimates for the reciprocal. More precisely, uniformly on
each such compact set,
\(\mathfrak d_N=-i(-1)^r[\sin(2\pi s)+O(N^{-1})]/(\varepsilon m)\).
The displayed level-dependent phase is retained.

P proves that the resolved complete geometric total moment is
nonreal when the total product is regular semisimple and loxodromic.
Thus (27) applies in a fixed small neighborhood of either supplied
nonreal moment. It establishes a nonzero scalar first-normal coupon
there. It does not assert that the angular kernel has a uniform
phase at that point or that the radial path selects its contribution.

## 5. Source and cycle scope

The positive radial path in (17),(21),(22) can also make any bounded
complex excursion and then return to its original positive end.
At each fixed meridian in the collar the densities are entire in s;
the original lower endpoint and the decaying positive end remain.
The arc estimates of Section2 prove the needed cutoff Stokes
statement, also for the regularized expression and fixed meridian
derivatives. This changes neither the projective angular cycle nor
any finite occupation cap.

For an angular subchain, (20) need not hold. Its polar coefficient
is exactly the integral of \(\mathfrak d_N\mathcal P_N(s,0)\)
on that subchain; it cannot be removed by applying the whole-source
identity locally. The common dual in (22) therefore does not supply
a transported angular window or a positive pairing. Nonvanishing
of \(\mathfrak d_N\) alone does not imply nonvanishing of its
pairing with \(\partial_\mu\mathcal P_N\).

Any separately prescribed scalar \(\chi_N(M)\) remains outside
these formulas in its original normalization and multiplies the
whole expression before the prescribed finite part or derivative.
No bound on its exponential rate is inferred. The new conclusion
is the exact common-angular dual and its off-real first-normal
unit. The original geometric relative-cycle coefficient and the
full closed-source lower bound remain unproved.

## Complete direct sources

* R: notes/research_actual_reduced_braid_source.md, 330 lines,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* P: notes/research_reduced_projective_occupation_source.md, 600 lines,
  SHA256 e9563cc9bdacb7a8afd15f1a199fd351ed963dbf8a07d761ecc69e4fa5ae6113.

Both complete directs were freshly read nontruncated in the active
author sequence; every used implication was checked. Only written
mathematics and text/hash operations were used. Frozen and public
files were not edited.
