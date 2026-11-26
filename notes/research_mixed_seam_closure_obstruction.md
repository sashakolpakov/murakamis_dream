# A crude seam closure estimate exceeds the available pair reserve

Research obstruction, 5 November 2026. The explicit three-step entry
and exit estimates do not uniformly fit inside the proved seam-pair
reserve, even at a homogeneous type-three reference. This concerns
an upper estimate for the common incoming potential. It does not
show that the common potential itself, the signed finite source, or
the full-period asymptotic has the wrong sign.

## 1. Original reference, phase and physical seam states

Use a homogeneous type-three cycle of length five, or any longer
homogeneous cycle. Its actual internal and outer critical coordinates
are all
\[
 p=1/3.
 \tag{1}
\]
Indeed, on the original logarithmic lift,
\(g'(p)=\tfrac12\log3+i\pi/6\) and
\(g'(2p)=\tfrac12\log3-i\pi/6\). Both original critical
equations vanish. The universal critical-point uniqueness theorem
identifies this solution with the geometric reference; periodic
repetition does not change it.

All reference heights are zero and no selection is allowed. Thus
the original hybrid graph is real on every target configuration in
this example. Fix the collar width \(\rho\) of the
[seam reduction](research_mixed_seam_boundary_potential_reduction.md).
Put the seam coordinate at \(x_0=\rho\), its two neighbors at
\(x_{-1}=x_1=1/2\), and every other coordinate at \(p\).
The seam attenuation is \(\lambda=0\). Its exact virtual halos
are both \(1/10\), so the boundary states of the one nonseam run
are
\[
 v_{\rm out}=(p,1/2,1/10),\qquad
 v_{\rm in}=(1/10,1/2,p).
 \tag{2}
\]
The first state is at layer zero and the second at layer two. The
physical nonseam run has at least four vertices. Its occupation
consists only of its two endpoint contributions. No separate target
copies have been incorrectly identified through the primitive
period-one reference.

Retain the calibrated primitive and allocated critical value
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 \phi(a,b)&=g(s+a)+g(s+b)-2g(s)+2\pi ias-g(a)-g(b),\\
 f(a,b)&=\Re\phi(a,b),\qquad M_0=f(p,p).
 \end{split}
 \tag{3}
\]
Here \(s\) is the unique original conditional root. At the reference,
\(\phi_a(p,p)=i\pi/3\), \(\phi_b(p,p)=-i\pi/3\).
The real geometric plane on every real target pair is therefore
exactly \(M_0\). In particular the original edge weight is
\(w(a,b)=f(a,b)-M_0\); it has no halo dependence in this example.
The [complete half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md)
applies to every pair used below. Neither an unsupported algebraic
phase nor an individual original-row rate is substituted for (3).

## 2. The explicit closure upper estimate

Use \(\theta=1/2\), the original occupation \(\omega\), and
\(t(a,b)=w(a,b)+(\omega(a)+\omega(b))/4\).
Let \(A^{[3]}(v)\) and \(E^{[3]}(v)\) be the literal three-step
baseline entry and exit costs for \(t\). They satisfy
\[
 H(v_{\rm out})-H(v_{\rm in})
 \le -E^{[3]}(v_{\rm out})-A^{[3]}(v_{\rm in})
                           -\tfrac12\Psi(v_{\rm out}).
 \tag{4}
\]
For the last term, close any incoming path to \(v_{\rm out}\)
by its three baseline exit symbols. The cyclic inequality counts
at least the three terminal occupations and gives
\(H(v_{\rm out})\le-E^{[3]}(v_{\rm out})-\Psi(v_{\rm out})/2\).
The other side uses \(H\ge A^{[3]}\). Thus (4) is a valid
strengthening of the simplest entry/exit bound.

Two of the six closing weights have baseline endpoints and vanish.
The four remaining action terms give the quantity
\[
 \mathcal C=4M_0-f(1/2,1/10)-f(1/10,p)
                       -f(p,1/10)-f(1/10,1/2).
 \tag{5}
\]
The exact occupations and all three occupation corrections are
\[
 \begin{gathered}
 \omega(p)=0,\quad \omega(1/10)=1/4000,\quad
 \omega(1/2)=21/4000,\quad \Psi(v_{\rm out})=11/2000,\\
 \text{entry plus exit correction}=23/8000,\qquad
 \Psi(v_{\rm out})/2=11/4000,\qquad
 \theta\Omega_A=21/8000.
 \end{gathered}
 \tag{6}
\]
In the last equality every interior physical nonseam coordinate is
baseline, so the endpoint-half bound is exact.

The seam-pair theorem retains the full finite gap \(G=7/25\).
Its reserved \(Q\) is zero at this real reference. Consequently
the upper proxy obtained from (4), after the actual component
occupation and the available pair reserve are subtracted, is
\[
 \mathcal P=\mathcal C-\frac{33}{4000}-\frac7{25}.
 \tag{7}
\]
The focused outward computation gives
\[
 \begin{split}
 0.88564961478&<\mathcal C<0.88564961479,\\
 0.59739961478&<\mathcal P<0.59739961479,
                      \qquad \mathcal P>59/100.
 \end{split}
 \tag{8}
\]
Thus this explicit closure estimate cannot be uniformly paid by
\(G+Q\), even after its extra occupation credit is retained.
Positivity of an upper bound is not a positive lower bound for the
actual boundary-potential difference. In particular (8) does not
contradict a sharper finite-depth or common-potential comparison.

The chosen collar endpoint and the real half endpoints cause no
source ambiguity. All inputs are covered by the closed half-period
theorem. Continuity also preserves the positive proxy for nearby
interior collar and half-period coordinates; no quantitative width
or new source-domain theorem is asserted here.

## 3. Exact root choice and reproducibility

For each of the five real pairs in (3) and (5), put
\(P=\cot\pi a\), \(Q=\cot\pi b\), and set
\[
 S=\frac{-(P+Q)+\sqrt{(P+Q)^2+4-4i(Q-P)}}2,
 \qquad
 s=\frac1{2\pi i}\log\frac{S+i}{S-i}.
 \tag{9}
\]
The checker uses interval arithmetic directly in this formula, not
a numerical root proposer. It verifies \(\Re S>0\),
\(|\Im S|<1\), and that \(s,s+a,s+b\) remain in the original
regular strip. The exact quadratic identity is
\[
 (S+P)(S+Q)-(P-i)(Q+i)
                  =S^2+(P+Q)S-1+i(Q-P)=0.
 \tag{10}
\]
It makes the exponential of the original derivative one. Its
enclosed logarithmic derivative has imaginary part strictly between
\(-\pi\) and \(\pi\), so its lift is exactly zero. The
[global cotangent-root theorem](research_mixed_global_cotangent_roots.md)
and its real half-endpoint extension then identify (9) with the
original conditional branch. The primitive in (3) fixes its absolute
action, including the chirp and both outer factorial allocations.

The focused checker binds the complete source and actual-reference
inputs, verifies the symbolic identities and exact occupation
arithmetic, and encloses (8) at 320 bits. It imports no diagnostic
file, root proposal, optimizer or sampled minimum.

```sh
python3 experiments/check_mixed_seam_closure_obstruction.py --precision 320
```

This is a failed sufficient estimate, not a counterexample to the
original finite conditional kernels or a volume asymptotic. All
previously completed source artifacts remain unchanged.
