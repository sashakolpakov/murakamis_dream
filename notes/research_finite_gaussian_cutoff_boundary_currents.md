# The original finite cutoff as a Gaussian relative integral with boundary currents

Private written proof, 18 November 2026.

The finite-dimensional Borel period of [G] has a derivative outside
its moving relative chain. A finite Laplace cutoff therefore is not
just the corresponding Gaussian relative integral. This note computes
the exact conversion, including every upper-boundary derivative.
The lower terms vanish by the actual coarea normalization, rather
than by removing the original endpoint.

## 1. Actual source and a common local domain

Keep the original highest cut, pivot, framing and fixed clocks of [G].
Write \(2d\) for its number of Gaussian variables and put
\(p=d+1\). The integer \(p\) here is only a derivative order.
It is not a collision multiplicity. Denote the normalized volume by
\[
                  \Omega=dx\wedge\Omega_K .
 \tag{1}
\]
The exact source formula of [G] is
\[
 J(Y,\xi)=\int_{\mathcal D_\xi(Y)}
       \widehat{\mathcal A}
           \bigl(\xi-\mathcal F(Y,x,X),Y,x,X,m\bigr)\,\Omega,
 \qquad
                 b(Y,\xi)=r(Y)\partial_\xi^pJ(Y,\xi).
 \tag{2}
\]
Every derivative in (2) is a derivative of the entire analytic
period, including the moving chain and its boundary. The original
raw amplitude and its Borel germ have not been replaced by a sum
chosen independently of the finite source.

Take a sufficiently small meridian disk about a fixed
\(Y_0\ne\alpha\) in [G]'s initial chart. Shrink it and a
\(\xi\)-disk so that the inverse soft coordinate and Gaussian
Morse coordinates are common there. In these coordinates
\[
 \mathcal F=t_0+\tfrac12q^Tq,\qquad
                  t_0=f(Y,x),\qquad x(Y,0)=0 .
 \tag{3}
\]
The construction in [G] gives \(J\) holomorphic jointly on this
product and
\[
                    J(Y,\xi)=O(\xi^p).
 \tag{4}
\]
In particular \(\partial_\xi^jJ(Y,0)=0\) for \(0\le j<p\).
These are the original values at the original lower endpoint.

Choose \(R\ne0\) so that the closed straight segment \([0,R]\)
and a small complex neighborhood lie in that \(\xi\)-disk.
All clock compacts are handled by the same shrinkage as in [G].
For \(\xi=tR\), \(0\le t\le1\), the chains are nested:
in (3), on the fixed real form selected by \(\sqrt R\),
\[
 \mathcal D_{tR}
  =\{\,t_0=Ra,\ q=\sqrt R\,v:
           a\ge0,\ v\in\mathbb R^{2d},\
                             a+|v|^2/2\le t\,\}.
 \tag{5}
\]
They are mapped back by the same holomorphic coordinates.
Thus \(\mathcal D_{tR}\subset\mathcal D_R\) as oriented
sublevel chains. Their genuine boundary portions remain
\(x=0\) and \(\mathcal F=tR\).

Use exactly [B]'s finite cutoff:
\[
             U_R(h,Y)=\frac1h\int_0^R
                                  e^{-\xi/h}b(Y,\xi)\,d\xi,
                              \qquad h\ne0 .
 \tag{6}
\]
This is an analytic finite integral on the common source domain.
No infinite ray, Borel sum, or finite-color equality is assumed.

## 2. Every upper-boundary jet

Define the finite boundary expression
\[
 E_R(h,Y)=
       \sum_{k=0}^{p-1}h^{-k-1}
                              \partial_\xi^{p-1-k}J(Y,R).
 \tag{7}
\]
Then integration by parts gives the exact identity
\[
 \boxed{\quad
 U_R(h,Y)=r(Y)e^{-R/h}E_R(h,Y)
       +r(Y)h^{-p-1}\int_0^R e^{-\xi/h}J(Y,\xi)\,d\xi .
 \quad}
 \tag{8}
\]
To check the signs and powers, one step is
\[
 \int_0^R e^{-\xi/h}J^{(j)}(\xi)\,d\xi
  =e^{-R/h}J^{(j-1)}(R)-J^{(j-1)}(0)
                +h^{-1}\int_0^R e^{-\xi/h}J^{(j-1)}(\xi)\,d\xi .
 \tag{9}
\]
Repeat this \(p\) times and multiply by \(r/h\).
All lower jets encountered have order less than \(p\), so (4)
makes them exactly zero. Every upper jet in (7) remains.
This proof integrates a holomorphic function of \(\xi\);
it never differentiates only the integrand while freezing
\(\mathcal D_\xi\).

Individually \(E_R\) is a finite Laurent polynomial in \(h\),
with possible pole order \(p\). It is not asserted holomorphic
at \(h=0\), nor identified with the different holomorphic
operator-defect current of [B]. Cancellations with the second
term in (8) are retained in the identity.

## 3. Nested Fubini gives the finite Gaussian integral

For each field point of \(\mathcal D_R\), define the finite
raw-amplitude cutoff
\[
 \mathcal A_{\rm fin}(h,\sigma;Y,x,X,m)
       =\frac1h\int_0^\sigma
              e^{-s/h}\widehat{\mathcal A}(s,Y,x,X,m)\,ds,
 \qquad \sigma=R-\mathcal F(Y,x,X).
 \tag{10}
\]
The integral follows the remaining segment in the same oriented
energy ray. The field point and its lifted coefficient arguments
are held fixed during this \(s\)-integration. On (5),
\(0\le\mathcal F/R\le1\), so \(|\sigma|\le|R|\);
all these paths lie in the common raw-amplitude Borel disk.
In particular
\(\mathcal A_{\rm fin}(h,0;Y,x,X,m)=0\) on the upper boundary.
No replacement by the formal amplitude
\(\sum h^j\mathcal A_j\) is made.

The exact relative Gaussian form of the original cutoff is
\[
 \boxed{\quad
 U_R(h,Y)=
 r(Y)h^{-p}\int_{\mathcal D_R(Y)}
           e^{-\mathcal F(Y,x,X)/h}
           \mathcal A_{\rm fin}
              (h,R-\mathcal F;Y,x,X,m)\,\Omega
                 +r(Y)e^{-R/h}E_R(h,Y).
 \quad}
 \tag{11}
\]
Here \(\mathcal D_R\) is the actual chain constructed from the
original source, with its \(x=0\) boundary, orientation and all
Gaussian normalization factors. The scalar \(r(Y)\) is unchanged.

For a direct Fubini proof, write \(\delta_t\) for its relative
coarea fiber and \(d\mathcal F\wedge\Omega_{\mathcal F}=\Omega\).
Equation (2) is
\[
 J(Y,\xi)=\int_0^\xi\int_{\delta_t}
       \widehat{\mathcal A}(\xi-t,Y,x,X,m)
                                      \,\Omega_{\mathcal F}\,dt .
 \tag{12}
\]
On the compact nested triangle \(0\le t/R\le\xi/R\le1\),
all integrands and coordinate Jacobians are bounded for fixed
\(h\ne0\). The vanishing coarea radius at \(t=0\) is integrable,
as explicitly shown by the \(t^{p-1}\) density in [G].
Ordinary Fubini is therefore applicable, and the orientations
are the increasing \(\xi\), then increasing \(t\), orientations.
It gives
\[
\begin{split}
 \int_0^R e^{-\xi/h}J(Y,\xi)\,d\xi
 &=\int_0^R\int_{\delta_t}
       \left[\int_t^R e^{-\xi/h}
          \widehat{\mathcal A}(\xi-t,Y,x,X,m)\,d\xi\right]
                                      \Omega_{\mathcal F}\,dt\\
 &=h\int_{\mathcal D_R}
          e^{-\mathcal F/h}
          \mathcal A_{\rm fin}(h,R-\mathcal F;Y,x,X,m)\,\Omega .
\end{split}
 \tag{13}
\]
The substitution \(s=\xi-t\) has positive orientation.
Combining (13) with (8) proves (11), including its power \(h^{-p}\).
Every integral is finite. This argument asserts no exchange of
an infinite quantum series with a Gaussian contour.

## 4. A normalization check and a local endpoint estimate

In the pure endpoint model with no Gaussian variables,
\(p=1\), \(f=zx\), \(r\) constant in \(\xi\), and
\(\widehat{\mathcal A}=1\), one has
\[
 J(\xi)=\xi/z,\qquad
 U_R=(r/z)(1-e^{-R/h}),\qquad
              \mathcal A_{\rm fin}(h,\sigma)=1-e^{-\sigma/h}.
 \tag{14}
\]
The integral term in (11) is
\[
        \frac rz(1-e^{-R/h})
                    -\frac{rR}{zh}e^{-R/h},
 \tag{15}
\]
and its upper jet is \(rR e^{-R/h}/(zh)\).
They cancel exactly to give (14). This checks the plus sign
of (7) and exhibits why the upper term cannot be dropped in
the identity.

On a compact smaller meridian/clock set, Cauchy's estimate
on a fixed neighborhood of \(R\) bounds the finitely many
jets in (7). Hence, for \(0<|h|\le1\),
\[
                |r(Y)E_R(h,Y)|\le C_R |h|^{-p}.
 \tag{16}
\]
On a facing sector
\(\operatorname{Re}(R/h)\ge\kappa |R|/|h|\),
their contribution to (11) obeys
\[
        |r e^{-R/h}E_R|
              \le C_R |h|^{-p}e^{-\kappa|R|/|h|}.
 \tag{17}
\]
This is only the absolute bound for these specified local
boundary jets. It neither bounds the Gaussian integral relative
to its value nor controls a large-\(R\) continuation.

At the unmarked specialization, since (11) equals the original
\(U_R\), every actual finite-shift operator satisfying [B]'s
coefficient and common-domain hypotheses still satisfies its identity
\(\mathcal P U_R=e^{-R/h}J_{\mathcal P,R}\), with the same
holomorphic current defined there. Applying \(\mathcal P\)
to only the integral term in (11) would omit the finite jets
in (7) and is not that identity.

## 5. Scope and proof directs

The construction provides the local current map from the
derivative coarea period to the original finite cutoff. It keeps
the soft lower boundary, all moving-chain derivatives, the raw
amplitude's remaining Borel segment, and every upper jet.
The explicit relative chain and the Borel cutoff have different
boundary descriptions; equations (8)--(13) are their exact adapter.

The nested source domain above is constructed for sufficiently
short \(R\). A global extension would have to transport the full
triangle of field points and remaining Borel segments on one
continued source domain, with its boundary jets. Neither the
existence of a regular critical-curve arc nor a nonzero local
minor supplies that transport. No physical finite-color identity,
geometric intersection or scalar lower is claimed here.

| Label | Complete proof source | SHA256 |
|---|---|---|
| G | notes/research_actual_source_finite_gaussian_borel_period.md | dda9ec95e7fc460dc965cc70c21d94e6d7e412bcdc4521b42c4137da3e00c9c8 |
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |

Both complete sources were read and every used implication checked.
G supplies the original compact relative period and its normalization;
B supplies the original finite cutoff and exact operator current.
All repeated integrations, moving-chain bookkeeping, Fubini
orientations and endpoint bounds are proved above.
Only written mathematics and source-text/hash operations were used.
Frozen notes and public manuscripts are unchanged.
