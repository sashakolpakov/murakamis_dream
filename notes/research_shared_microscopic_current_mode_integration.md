# Integrating a shared microscopic current in the actual endpoint modes

Private written proof, 16 November 2026.

The original microscopic current integrates one common real parameter
at all incidences of its removed vertex. On buffered physical windows,
its exact full-jet representatives admit a uniform integrated estimate
sharper than the supremum of their separate endpoint factors. The gain
is logarithmic. A nonzero integrated coefficient for every incidence
number at least three, and a surviving zero-frequency term for two
incidences, preclude an exponential improvement from this local
integration alone.

These are local source statements. The actual remaining traces,
outside rows, interfaces and connecting contours are retained. No
whole-current rate or nonzero original closing is inferred.

## 1. The original current and its local representatives

Fix an integer \(n\), a real \(A>0\), and an incidence number \(d\ge1\),
all independent of \(N\). Put
\[
 \eta=(-1)^{N-1},\quad
 C_{N,n}=e^{\pi i n(N-1)^2/(4N)},\quad
 w_N(\alpha)=2\cosh(\alpha/N),\quad
 C_N(x)=2\cos(2\pi x+\pi/N).
 \tag{1}
\]
The exact original unit-charge current is
\[
 V_{n,1}^{A/N}[f]
       =\int_0^{A/N}\rho_{N,n,1}(h)f(2\cosh h)\,dh,
\]
\[
 \rho_{N,n,1}(h)=
 \frac{i\eta N^2C_{N,n}}{2\pi}
 \frac{\sinh h\,e^{inN(\pi^2-h^2)/(4\pi)}
                    \sinh(nNh/2)}
      {\cosh^2(Nh/2)}.
 \tag{2}
\]
With the common variable \(\alpha=Nh\), define
\[
 \Theta_{N,n}=\frac{i\eta C_{N,n}e^{inN\pi/4}}{2\pi},\qquad
 q_{N,n}(\alpha)=
 N\sinh(\alpha/N)\frac{\sinh(n\alpha/2)}{\cosh^2(\alpha/2)}
                       e^{-in\alpha^2/(4\pi N)}.
 \tag{3}
\]
Then \(\rho(h)\,dh=\Theta_{N,n}q_{N,n}(\alpha)\,d\alpha\)
exactly. In particular \(|\Theta_{N,n}|=1/(2\pi)\). There is
no discarded crossing phase or denominator alias.
For \(n=0\), every integral below is exactly zero.

For each incidence \(i\), choose the actual sharp baseline and one
designated-half representative \(H_{i,N}^{\sigma_i}(x_i,\alpha)\)
of the endpoint kernel
\(K_N(w_N(\alpha),C_N(x_i))\).
Use fixed nested real windows with buffers inside \(0<\Re x_i<1/2\),
any prescribed finite heights, and a compact part of the designated
half \(\sigma_i\Im x_i\ge0\). All estimates hold on smaller buffers.
No fold or endpoint extension is needed here.

The pinned actual connection and repair theorems give, for real
\(0\le\alpha\le A\), uniformly on these domains,
\[
 H_{i,N}^{\sigma_i}(x_i,\alpha)
       =g_\alpha(Ns_i)+O_{\mathrm{hol},x_i}(N^{-1-\epsilon}),
 \qquad s_i=\frac{\sin(\pi x_i)}{\pi},
 \tag{4}
\]
for some \(\epsilon>0\). Every fixed spatial derivative has this
error. The value \(\epsilon\) may be decreased for the finite set of
windows. The logarithm of \(s_i\) is its continuation from positive
real \(s_i\), and is bounded on the chosen compacts. Here
\[
 \mathfrak k_\pm(\alpha)=
 \frac{\Gamma(\pm i\alpha/\pi)}
      {\Gamma(1/2\pm i\alpha/(2\pi))^4},\qquad
 g_\alpha(Ns)=
 \frac{\mathfrak k_+(\alpha)e^{i\alpha\log(Ns)/\pi}
       +\mathfrak k_-(\alpha)e^{-i\alpha\log(Ns)/\pi}}{Ns}.
 \tag{5}
\]
The combined expression is removable at \(\alpha=0\).
No endpoint-parameter derivative estimate for the error in (4)
is assumed or used.

Define the integrated local representative
\[
 \mathcal J_{N,n,d}(\mathbf x)=
 \Theta_{N,n}\int_0^A q_{N,n}(\alpha)
             \prod_{i=1}^dH_{i,N}^{\sigma_i}(x_i,\alpha)\,d\alpha .
 \tag{6}
\]
The same \(\alpha\) occurs in all \(d\) factors. Its actual polynomial
counterpart is
\[
 \mathcal Q_{N,n,d}(\mathbf Z)=
 \int_0^{A/N}\rho_{N,n,1}(h)
                  \prod_{i=1}^dK_N(2\cosh h,Z_i)\,dh.
 \tag{7}
\]
At every covered physical grid tuple, (6) and (7) have exactly the
same values and mixed first spectral normals. This follows from
the exact individual repairs, their product rule, and differentiation
under a finite integral. Identifying several \(Z_i\)'s is also allowed:
the ordinary product rule retains the one full normal of that shared
color. An additional joint spectator independent of \(\alpha\) remains
inside its subsequent original trace.

## 2. Uniform integrated upper bounds

Put \(L=\log N/\pi\), and consider sufficiently large \(N\).

**Theorem 1.** For every fixed spatial multi-index \(\beta\),
\[
 |\partial_{\mathbf x}^{\beta}\mathcal J_{N,n,d}|
 \le C_\beta N^{-d}
 \begin{cases}
 L^{-1},&d=1,\\
 1,&d=2,\\
 L^{d-3},&d\ge3.
 \end{cases}
 \tag{8}
\]
The constants are uniform on the prescribed buffered compacts and
at both parities. They may depend on \(n,A,d\) and the domains.
The same theorem holds with any or all representatives replaced by
their actual baselines.

*Proof.* Factor the density as
\[
 q_{N,n}(\alpha)=\alpha^2b_{N,n}(\alpha),\qquad
 b_{N,n}(0)=n/2.
 \tag{9}
\]
On a fixed complex neighborhood of \([0,A]\), small enough to avoid
the zeros of \(\cosh(\alpha/2)\), these are holomorphic with uniformly
bounded derivatives, and
\[
 b_{N,n}\longrightarrow
 b_n(\alpha)=\frac{\sinh(n\alpha/2)}
                    {\alpha\cosh^2(\alpha/2)}
 \quad\hbox{uniformly with every fixed derivative.}
 \tag{10}
\]
The value at zero is removable.

Let \(\ell_i=\log s_i/\pi\). The Gamma residues are
\(\mathfrak k_+=-i/(\pi\alpha)+O(1)\) and
\(\mathfrak k_-=i/(\pi\alpha)+O(1)\).
Consequently there are holomorphic, uniformly bounded coefficients
\(a_i,b_i\), with all fixed derivatives on slightly smaller domains,
such that exactly
\[
 Ns_i\,g_\alpha(Ns_i)
   =a_i(\alpha)\frac{\sin(L\alpha)}{\alpha}
                          +b_i(\alpha)\cos(L\alpha),
 \qquad a_i(0)=2/\pi .
 \tag{11}
\]
Explicitly,
\[
 a_i=i\alpha[
       \mathfrak k_+e^{i\ell_i\alpha}
                   -\mathfrak k_-e^{-i\ell_i\alpha}],\qquad
 b_i=\mathfrak k_+e^{i\ell_i\alpha}
                   +\mathfrak k_-e^{-i\ell_i\alpha}.
 \tag{12}
\]
Their apparent singularities at zero cancel. Choose the complex
parameter neighborhood smaller if necessary to avoid all other
Gamma singularities. No large-\(N\) parameter derivative is involved.

Expanding the product in (11), the terms with \(j\) sine-over-parameter
factors have integrals of the form
\[
 \int_0^A \alpha^{2-j}F_{j,N}(\alpha,\mathbf x)
        \sin^j(L\alpha)\cos^{d-j}(L\alpha)\,d\alpha,
 \tag{13}
\]
where the finite family of \(F_{j,N}\)'s and their fixed derivatives
are uniformly bounded. For \(j\le2\), their absolute integrals are
bounded. For \(j\ge4\), split at \(1/L\), use
\(|\sin(L\alpha)|\le\min(L\alpha,1)\), and integrate to obtain
\(O(L^{j-3})\).

For \(j=3\), the trigonometric polynomial
\(\sin^3 u\cos^{d-3}u\) is a finite sum of nonzero sine harmonics.
Write
\(F_{3,N}(\alpha)=F_{3,N}(0)+\alpha G_{3,N}(\alpha)\).
The \(G\)-term has bounded absolute integral. Each remaining integral
\(\int_0^A\sin(kL\alpha)\,d\alpha/\alpha\) is uniformly bounded:
after rescaling, its tail is bounded by integration by parts.
This proves (8) for \(d\ge2\).

When \(d=1\), (13) consists of a sine with smooth coefficient
\(\alpha F_{1,N}\), and a cosine with smooth coefficient
\(\alpha^2F_{0,N}\). One integration by parts gives \(O(L^{-1})\),
including its endpoint at \(A\); both coefficients vanish at zero.

Finally (4), the coalesced bound \(|g_\alpha(Ns_i)|\le CL/N\),
and the product rule show that replacing the Gamma product by the
actual product costs
\[
 O_\beta(N^{-d-\epsilon}L^{d-1}).
 \tag{14}
\]
This is smaller than every scale in (8). The same argument applies
to every fixed spatial derivative: differentiating (11)--(13) changes
only uniformly bounded coefficient functions. The pinned repair
estimates supply the corresponding actual derivative error in (14).
\(\square\)

## 3. The retained endpoint, zero-frequency term and small-parameter layer

The upper bound is not an exponential improvement. Its leading
terms can be specified without discarding the endpoint \(A\).

For \(d=1\), twice integrating the two individual exponentials gives
\[
 \begin{split}
 \mathcal J_{N,n,1}(x)
 =\frac{\Theta_{N,n}}{Ns}\frac{q_{N,n}(A)}{iL}
 \bigl[
 \mathfrak k_+(A)e^{iA(L+\ell)}
       -\mathfrak k_-(A)e^{-iA(L+\ell)}
 \bigr]+O_{\mathrm{hol},x}(N^{-1}L^{-2}).
 \end{split}
 \tag{15}
\]
Indeed \(q_{N,n}\mathfrak k_\pm e^{\pm i\ell\alpha}\) are smooth
with uniformly bounded derivatives and have value zero at \(\alpha=0\).
Their second integration by parts has bounded endpoint and integral
remainders. Equation (14) is absorbed in the error of (15).
The displayed endpoint coefficient may oscillate or vanish; no
lower bound is assigned to it.

For \(d=2\), let
\[
 q_n(\alpha)=\alpha\frac{\sinh(n\alpha/2)}{\cosh^2(\alpha/2)},
\]
\[
 B_{n,A}(s_1,s_2)=
 \int_0^A q_n(\alpha)\mathfrak k_+(\alpha)\mathfrak k_-(\alpha)
 \left[e^{i\alpha\log(s_1/s_2)/\pi}
       +e^{-i\alpha\log(s_1/s_2)/\pi}\right]\,d\alpha .
 \tag{16}
\]
The integrand is removable at zero. Then
\[
 \mathcal J_{N,n,2}
 =\frac{\Theta_{N,n}}{N^2s_1s_2}
                     [B_{n,A}(s_1,s_2)+O_{\mathrm{hol},\mathbf x}(L^{-1})].
 \tag{17}
\]
The two equal-sign modal products have frequencies \(\pm2L\).
Their coefficients, including \(q_{N,n}\), are smooth at zero, so
integration by parts bounds them by \(O(L^{-1})\). The opposite-sign
products have frequency zero in \(L\) and give (16). Replacing
\(q_{N,n}\) by \(q_n\) costs \(O(N^{-1})\); (14) is also smaller
than the displayed error. If \(s_1=s_2>0\) and \(n\ne0\), then
\[
 B_{n,A}(s_1,s_1)
       =2\int_0^Aq_n(\alpha)|\mathfrak k_+(\alpha)|^2\,d\alpha
 \tag{18}
\]
is nonzero and has the sign of \(n\). This is one coefficient
identity for the whole two-incidence operator, not a positivity
claim for its later closing.

**Theorem 2.** For every \(d\ge3\), uniformly on the same spatial
compacts and with every fixed spatial derivative,
\[
 \boxed{\quad
 \frac{N^d}{\Theta_{N,n}L^{d-3}}\mathcal J_{N,n,d}
       \longrightarrow
 \frac{n}{2}\left(\frac2\pi\right)^d
                           \frac{\mathcal C_d}{\prod_i s_i},
 \quad}
 \tag{19}
\]
where
\[
 \mathcal C_3=\pi/4,\qquad
 \mathcal C_d=\int_0^\infty t^{2-d}\sin^d t\,dt>0
                                      \quad(d\ge4).
 \tag{20}
\]
For \(n\ne0\) the limit is nowhere zero on these compacts.

*Proof.* Suppose first \(d\ge4\). Only the term \(j=d\) of (13)
can contribute after division by \(L^{d-3}\). Each term with
\(j<d\) tends to zero by the bounds just proved.
In the remaining term set \(t=L\alpha\). Its normalized integrand is
\[
 {\bf1}_{t\le AL}\,t^{2-d}\sin^d t\,
 b_{N,n}(t/L)\prod_i a_i(t/L).
 \tag{21}
\]
The absolute majorant \(C t^{2-d}|\sin t|^d\) is integrable for
\(d\ge4\), both at zero and infinity. The coefficient tends uniformly
on compact \(t\)-intervals to \((n/2)(2/\pi)^d\). Dominated convergence
proves (19). It applies after every fixed spatial derivative as well,
using the coefficient bounds; the actual error (14), divided by
\(N^{-d}L^{d-3}\), is \(O(N^{-\epsilon}L^2)\).

For \(d=3\), all \(j<3\) trigonometric polynomials in (13) have
nonzero frequencies only, since their total degree is odd. Their
coefficients are smooth at zero; integration by parts gives
\(O(L^{-1})\). For the remaining term put
\(F_N=b_{N,n}\prod_i a_i\), so \(F_N(0)=(n/2)(2/\pi)^3\).
The difference \([F_N(\alpha)-F_N(0)]/\alpha\) has uniformly bounded
first derivative and hence contributes \(O(L^{-1})\). The constant
term is
\[
 F_N(0)\int_0^{AL}\frac{\sin^3 t}{t}\,dt
                   \longrightarrow F_N(0)\pi/4.
 \tag{22}
\]
For completeness, integration by parts gives a uniform \(O(R^{-1})\)
tail for each \(\sin(kt)/t\). Its integral is \(\pi/2\) for \(k>0\):
exponential damping gives
\(\int_0^\infty e^{-\varepsilon t}\sin(kt)\,dt/t
=\arctan(k/\varepsilon)\), and the same tail estimate removes the
damping. Now \(\sin^3t=(3\sin t-\sin3t)/4\), proving (22).
This is conditional Dirichlet convergence, not absolute dominated
convergence. The argument and actual error bound apply to spatial
derivatives too.

For even \(d\ge4\), positivity in (20) is immediate. For odd \(d\ge5\),
pair successive intervals of length \(\pi\). Each pair is the integral
of \(\sin^d u>0\), \(0<u<\pi\), times
\((2k\pi+u)^{2-d}-((2k+1)\pi+u)^{2-d}>0\).
Absolute convergence permits these pairings. Thus \(\mathcal C_d>0\).
\(\square\)

## 4. Exact source placement and limits of the estimate

Equations (6)--(7) are a local representation of the original current
at one removed vertex, with arbitrary fixed incidence number. The
crossing power \(n=0\) makes this removed current zero; it places no
restriction on powers at surviving vertices.
The cut height \(A/N\) is retained exactly, including the term (15).
Changing \(A\) or joining adjacent height pieces is a different
decomposition whose endpoint terms must be added with their original
orientations.

At each surviving traced color, the pinned one-sided construction
expresses the original physical-window trace as its two exterior
half-contours plus its real interface. Integrating that exact identity
in \(\alpha\) commutes with all finite traces and contour integrals.
The integrated interface keeps its sharp exponential bound because
\(\int_0^A|q_{N,n}(\alpha)|\,d\alpha\le C\). All original vertical
half-sides, rational aliases and physical rows outside the windows
remain. The common surviving spectator has not been removed or
assigned a norm bound here.

Thus the nonzero limit (19) is a local integrated multiplier; it is
not a nonzero coefficient for the original scalar. Nor do (8)--(19)
bound the ordinary canonical polynomial at off-grid colors. Its
exact local full jets are represented by (6), and that is the scope
of the estimate.

Several current vertices may have edges between them. Their factors
\(K_N(w_N(\alpha),w_N(\beta))\), or other parameter-dependent joint
sources, are additional shared amplitudes. This proof does not omit
them or silently extend (19) to them. Likewise it supplies no bound
for a subsequent outer turn. For a parent's fixed height \(H>0\),
the full current ranges over \(0\le\alpha\le NH\); the theorem concerns
its bounded microscopic segment only.

The supremum bound for \(d\) separate factors is
\(O(N^{-d}(\log N)^d)\). Integrating their actual common parameter
improves this to (8), while (17)--(20) show why the improvement
cannot generally be exponential in \(N\). Shared signs create a
zero-frequency sector, and the coalescing layer
\(\alpha\asymp1/\log N\) has a nonzero integrated coefficient.
Any strict parent-action comparison still requires the complete
source and its retained currents.

## 5. Coverage and direct sources

The full-current note already supplies the exact integration and
finite charge convolution. The grouped Ward-current matching formula
and the vertical cotangent regrouping identity concern different
current representations; their complete texts were checked for
overlap. Neither supplies the shared Gamma-mode integral above.
They are coverage pointers, not proof dependencies.

The following complete direct sources were read at these hashes,
with their used normalization, actual-connection and full-jet
implications checked:

* [Original full-period current](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595.
* [Actual tall Gamma connection](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.
* [Exact one-sided full-jet window assembly](research_sharp_endpoint_one_sided_window_assembly.md),
  SHA256 163d4cf2fc98648c0739152dbb463f2ad8f19d58b34b31d9184469847e60e541.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build was run.
Previously adopted notes and public manuscripts were unchanged.
