# A fixed-contour continuation of the full three-vertex conditional sum

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The [full-circle theorem](research_mixed_three_conditional_circle.md)
sums the entire original conditional support at physical integer
neighbors. Here we construct an exact, specified holomorphic continuation
of that coefficient near every point of its real neighbor box. The
construction retains a fixed cut and all connecting contours. It does
not identify different off-grid continuations or prove a global
mixed-word lower bound.

## 1. The exact continuation

Write \(K=[1/5,9/20]^2\), \(r=e^{-2\pi i/N}\), and
\(p_a(z)=\prod_{h=1}^a(1-r^h z)\). The original coefficient is
\[
 L_0(a,b)=N[z^a]p_a(z)p_b(z).
 \tag{1}
\]
This identity includes the entire physical conditional support, by
[the exact finite-sum calculation](research_mixed_conditional_leg_sum.md).
Let \(G_N\) be the actual sine-factorial interpolation in
[the factorial construction](exact_factorial_interpolation_and_complex_contours.md).
For a complex neighbor \(\alpha\), put
\[
 \begin{split}
 s(w)&=\frac12+\frac{iw}{2\pi},\\
 \mathcal P_N(\alpha,w)
 &=\exp\!\left(\frac{N\alpha w}{2}
       -\frac{\pi iN\alpha^2}{2}-\frac{\pi i\alpha}{2}\right)
       \frac{G_N(N(s(w)+\alpha))}{G_N(Ns(w))}.
 \end{split}
 \tag{2}
\]
At every nonnegative integer \(a=N\alpha\), the factorial recurrence
gives exactly
\[
 \mathcal P_N(a/N,w)=p_a(-e^w).
 \tag{3}
\]
Indeed each factor is
\(2i e^{-\pi i(s+h/N)}\sin\pi(s+h/N)
=1+e^{w-2\pi ih/N}\). Their exponential product is the factor
displayed in (2). Thus (2) has no unspecified periodic multiplier.

Fix a real reference \((\alpha_*,\beta_*)\in K\). The construction
below chooses real constants \(\eta_0\ne0\) and \(\theta_-\), independent
of \(N,\alpha,\beta\). On a sufficiently small fixed complex polydisk
\(U_*\) about the reference, define
\[
 \begin{split}
 \Gamma_*&=\{\eta_0+i\theta:
                         \theta_-\le\theta\le\theta_-+2\pi\},\\
 \mathcal L_{N,*}(\alpha,\beta)
 &=\frac{N e^{\pi iN\alpha}}{2\pi i}
       \int_{\Gamma_*}e^{-N\alpha w}
             \mathcal P_N(\alpha,w)\mathcal P_N(\beta,w)\,dw.
 \end{split}
 \tag{4}
\]
The path is oriented upward. We choose
\(|\Im\alpha|,|\Im\beta|<|\eta_0|/(4\pi)\), so that all factorial
arguments on this path stay off the real axis. Consequently (4) is
holomorphic in both neighbors. At every physical pair
\((a/N,b/N)\in U_*\), (3) and the literal Cauchy coefficient formula
give
\[
                   \mathcal L_{N,*}(a/N,b/N)=L_0(a,b).
 \tag{5}
\]
At noninteger neighbors the integrand need not be periodic in
\(\Im w\). Formula (4) uses its displayed fixed lift; its two cut
ends are never identified during a deformation.

## 2. A bound for the exact factorial away from its real divisors

**Lemma 1.** For a compact set \(E\subset\mathbb C\setminus\mathbb R\)
and every fixed \(j\ge1\),
\[
 \sup_{z\in E}\left|\partial_z^j\log G_N(Nz)\right|\le C_{E,j}N
 \qquad(N\ge N_E).
 \tag{6}
\]
Logarithmic derivatives are single-valued. The meromorphic factorial
has no zero or pole on \(\mathbb C\setminus\mathbb R\).

*Proof.* The defining Gamma product continues meromorphically as
\[
 G_N(v)=(2\pi/N)^v\Gamma(v+1)
  \prod_{k\ge1}
   \frac{\Gamma(Nk+v+1)}{\Gamma(Nk-v)(Nk)^{2v+1}}.
 \tag{7}
\]
Its logarithmic tail is locally uniformly convergent off the real
Gamma divisors; these are all real. In particular its nonreal values
are nonzero. On compact nonreal sets every one of the finitely many
potentially nonpositive scaled Gamma arguments lies in a fixed closed
sector \(|\arg z|\le\pi-\varepsilon_E\). For all remaining arguments
one uses a common right-half-plane sector. The same Stirling/digamma
remainder argument as in the factorial construction therefore applies.
Differentiating (7) gives
\[
 \begin{split}
 \frac1N\partial_z\log G_N(Nz)
 &=\log(2\pi/N)+\psi(Nz+1)\\
 &\quad+\sum_{k\ge1}
 [\psi(N(k+z)+1)+\psi(N(k-z))-2\log(Nk)].
 \end{split}
 \tag{8}
\]
The leading terms are \(\log(2\pi)+\Log z\) and
\(\Log(k+z)+\Log(k-z)-2\log k\). The latter are \(O_E(k^{-2})\)
for large \(k\). Their first remainders are
\((2N)^{-1}((k+z)^{-1}-(k-z)^{-1})\), also summable; the further
remainders are bounded by \(C_E N^{-2}k^{-2}\). This proves (6) for
\(j=1\). Differentiation on a slightly larger nonreal compact set,
or Cauchy's formula, proves every fixed higher order. No asymptotic
continuation through a factorial zero has been used. \(\square\)

In particular, on a fixed path (4) and a sufficiently small neighbor
polydisk, its exact integrand \(\mathcal I_N\), including the carrier,
satisfies
\[
 |\partial_\alpha\log\mathcal I_N|
       +|\partial_\beta\log\mathcal I_N|\le C_*N.
 \tag{9}
\]
This estimate will be used only on the unchanged far arc. The central
arc has the stronger regular-strip symbol below.

## 3. The central symbol and the selected critical point

Use the notation of Section 6 of the full-circle theorem:
\[
 \begin{split}
 h(\alpha,\beta,w)&=
   \int_0^\alpha\Log(1+e^{w-2\pi ix})\,dx
  +\int_0^\beta\Log(1+e^{w-2\pi ix})\,dx-\alpha w,\\
 q_0(\alpha,\beta,w)&=\frac12\bigl[
  \Log(1+e^{w-2\pi i\alpha})+
  \Log(1+e^{w-2\pi i\beta})-2\Log(1+e^w)\bigr],\\
 Q(\alpha,\beta)&=h(\alpha,\beta,w_c)+\pi i\alpha,
                  \qquad h_w(\alpha,\beta,w_c)=0.
 \end{split}
 \tag{10}
\]
The logarithms are those on the selected arc. For real neighbors in
\(K\), the whole-circle theorem gives a unique \(w_c\), with
\[
 |\Re w_c|<\log3,\qquad
 \Im w_c\in[\pi\min(\alpha,\beta),\pi\max(\alpha,\beta)],
 \qquad \Re h_{ww}(w_c)>1/10800.
 \tag{11}
\]
Its holomorphic continuation exists on a fixed neighborhood of each
real reference. On a small fixed central arc, all of
\(s,s+\alpha,s+\beta\) have real parts strictly between zero and
one, including when \(\Re w\) crosses zero. Thus the regular
factorial expansion gives the exact-symbol asymptotic
\[
 e^{-N\alpha w}\mathcal P_N(\alpha,w)\mathcal P_N(\beta,w)
       =e^{Nh(\alpha,\beta,w)+q_0(\alpha,\beta,w)}
                              (1+O(N^{-1})).
 \tag{12}
\]
It is uniform and holomorphic with every fixed derivative on smaller
compact sets. The square-root factor of the individual ratio (2) is
\(e^{-\pi i\alpha/2}\sqrt{\sin\pi(s+\alpha)/\sin\pi s}\), which
is exactly the corresponding factor in \(e^{q_0}\). These marks
continue from the original central sine strip.

The actual, unsquared critical equation fixes the endpoint symbol:
\[
 h_w=-q_0/(\pi i)-\alpha,
                 \qquad q_0(\alpha,\beta,w_c)=-\pi i\alpha.
 \tag{13}
\]
It also fixes the absolute action. With
\(g(z)=J(z)+i\pi(z-z^2)/2\), one has identically on this chart
\[
 h(\alpha,\beta,w)+\pi i\alpha
  =g(s+\alpha)+g(s+\beta)-2g(s)+2\pi i\alpha s.
 \tag{14}
\]
This follows by integrating \(g'(s+x)=\Log(1+e^{w-2\pi ix})\),
not by comparing unspecified critical constants.

## 4. The full far arc and both connecting currents

**Lemma 2.** The fixed contour in (4) and its polydisk can be chosen
so that only one fixed central subarc needs deformation. Its two
connecting segments and the entire remaining lifted circle have
absolute bound
\[
            N^C\exp\{N(\Re Q(\alpha,\beta)-d_*)\},
                     \qquad d_*>0,
 \tag{15}
\]
uniformly on a smaller complex polydisk and at both level parities.

*Proof.* At the real reference write
\(w_*=\eta_*+i\theta_*\). Choose a small angular half-width
\(\varepsilon>0\) so that the arc
\(|\theta-\theta_*|\le2\varepsilon\) lies in the regular central
factorial chart. Choose the cut \(\theta_-=\theta_*-\pi\).
The full-circle theorem gives a fixed strict loss on the complement
of \(|\theta-\theta_*|<\varepsilon\) at radius \(e^{\eta_*}\).
The same statement holds for its continuous logarithmic potential.
One may obtain it by taking physical neighbor approximants in that
theorem, or directly by its paired-root integral comparison.

That potential is continuous on the full compact circle, also at
\(\eta_*=0\). To see the only possible issue explicitly, near a
factor zero its integrand differs by a bounded smooth term from
\(\log\sqrt{\eta^2+v^2}\); its integral over a moving finite interval
has uniform modulus of continuity \(O(d|\log d|)\). Away from these
finitely many local zero charts ordinary uniform continuity applies.
Consequently choose a fixed nonzero \(\eta_0\) sufficiently close to
\(\eta_*\) that the strict far-arc loss remains. The central endpoints
at \(\theta_*\pm\varepsilon\), and the segments between heights
\(\eta_0\) and \(\eta_*\), retain the same kind of strict loss by
the regular central phase and continuity. This choice works even
when the original critical radius is exactly one.

For each sufficiently large \(N\), choose physical
\(a_N/N,b_N/N\in K\) within \(O(N^{-1})\) of the reference,
using inward rounding at a boundary of \(K\). On the unchanged
circle at \(\eta_0\ne0\), every polynomial factor is uniformly
nonzero. Smooth Riemann sums there give its logarithmic modulus
equal to \(N\) times the continuous potential plus \(O(1)\),
uniformly around the entire circle. Hence the exact physical
integrand has the required strict far-arc bound.

Now shrink the fixed complex polydisk. Integrating (9) from these
physical approximants to \((\alpha,\beta)\) changes the logarithmic
modulus by at most \(C_*N\) times their distance. The critical action
also changes continuously. Choosing the polydisk radius sufficiently
small therefore preserves a positive part of the strict gap. On
the two central connecting segments use (12), whose regular-strip
domain remains fixed, and the same continuity argument. This proves
(15), without a uniform asymptotic assertion through a far-arc
factorial branch wall. \(\square\)

In applying the lemma, replace the central vertical segment at
\(\Re w=\eta_0\) by the parallel segment through the actual critical
point, together with the two horizontal connecting segments at its
fixed angular endpoints. Cauchy's theorem is valid on their entire
small regular rectangle for the same exact integrand (2). The rest
of \(\Gamma_*\), including its two cut ends, is unchanged. Thus
there is no off-grid periodicity assertion and no missing seam current.

## 5. The holomorphic full-conditional packet

**Theorem 3.** For every \((\alpha_*,\beta_*)\in K\), there are a
fixed contour (4), a complex neighborhood \(U_*\), and a smaller
neighborhood on which
\[
 \boxed{\quad
 \mathcal L_{N,*}(\alpha,\beta)
  =\sqrt N\,
       \frac{e^{-\pi i\alpha}}
            {\sqrt{2\pi h_{ww}(\alpha,\beta,w_c)}}
       e^{NQ(\alpha,\beta)}(1+O(N^{-1})).\quad}
 \tag{16}
\]
The square root continues from the positive-real-part Gaussian
branch in (11); the coefficient is nonzero. The normalized remainder
is holomorphic, uniform, and has every fixed derivative bound on
smaller neighborhoods. Formula (5) holds exactly, so (16) is a
continuation of the full original conditional coefficient, including
every physical support row. A finite family of such patches covers
\(K\).

*Proof.* Lemma 2 disposes of the unchanged far arc and both joining
segments with an exponential gap. On the central segment through
\(w_c\), (11)--(12) give the usual vertical Gaussian, whose
quadratic term is \(-h_{ww}\theta^2/2\). Its contribution, with the
literal factor \(N/(2\pi i)\) and \(dw=i\,d\theta\), is
\(\sqrt{N/(2\pi h_{ww})}\,e^{q_0(w_c)}e^{NQ}\).
Equation (13) gives (16). Odd local Gaussian corrections integrate
to zero, leaving relative \(O(N^{-1})\). Uniform holomorphy on a
slightly larger polydisk gives the normalized derivative claims.
Compactness supplies the finite cover. \(\square\)

For the exact conditional transfer \(T_0=L_0/P_a^2\), one may divide
(4) by the nonzero marked factorial interpolation of \(P_a^2\) on
the same regular neighbor strip. This preserves exact physical-grid
agreement and yields its corresponding holomorphic packet.

Two different choices of fixed cut or off-grid continuation are not
claimed to be identical. On an overlap containing the same real
reference branch, the construction uses the same exact central
integrand; their difference consists of gapped contour pieces and
is exponentially smaller there. In particular this local theorem
does not license moving an outer neighbor contour across a patch
boundary without retaining its exact continuation. Nor does it
estimate the residual neighbor sum or the type-four conditional
functional. These remain separate global cancellation problems.

## 6. Reproduction

Run `python3 experiments/check_mixed_three_conditional_complex_neighbors.py`.
The focused checker verifies the exact interpolation phases, local
symbol and Gaussian normalization, and finite shifted-factorial
values off the real axis. It checks current provenance of the exact
conditional and full-circle inputs. The global complex-neighborhood
claim follows from Lemmas 1--2, not from those finite diagnostics.
