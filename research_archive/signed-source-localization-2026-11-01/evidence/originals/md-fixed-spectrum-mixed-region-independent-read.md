# Independent verification of the mixed spectral-region bound

This record concerns the complete proof in md-fixed-spectrum-mixed-region-bound.md. It checks the original local numerator, its shared coefficient, and the restricted full-Hermite terms. No numerical tests or global remainder hypothesis are used.

## 1. The local numerator has the stated number of factors

The interval from row \(i\) to row \(i+k\) contains \(k+1\) diagonal rows. The characteristic polynomial of the triangular face matrix is exactly
\[
 \prod_{j=0}^{N-1}(\sigma-c_j)=\chi_N(\sigma).
\]
Clearing the resolvent entry leaves the interval continuant and precisely
\[
                         N-(k+1)=d-k
\]
unused row factors. A skipped row inside the interval is already included in the two-step term of that continuant. Multiplying another \(\chi_N\), or another product of internal diagonal factors, would therefore be incorrect. The displayed recurrence in the source note includes neither extra factor and is valid at all spectral collisions.

Multiplication by \(x+y\) has coefficient \(\ell^1\) norm at most two; multiplication by \(xy\) preserves it. On the real spectral interval, \(s_j^2\le4\), \(s_js_{j-1}\le4\), and \(|\sigma-c_j|\le4\). Thus the continuant norm obeys
\[
 M_k\le8M_{k-1}+16M_{k-2},\qquad M_0=1,\quad M_1\le8.
\]
For \(B=4(1+\sqrt2)\), one has \(B^2=8B+16\) and \(B>8\). Induction gives \(M_k\le B^k\). The unused factors supply at most \(4^{d-k}\), so each original coefficient is at most \(B^d\). No normal derivative is discarded: this is an estimate of the entire original polynomial numerator.

## 2. The mixed shared coefficient retains its targets

At \(k\) specified crossing regions, the signed positive-end proof gives a coefficient bound \(A_\delta N^3e^{N\omega(\delta)}\). At the remaining \(r-k\) regions, the preceding estimate gives \(B^d\). There are at most \(N^{3r}\) formal monomial selections before imposing the one original shared coefficient. Hence
\[
 \|D_N\|_{\mathcal Q_J}
 \le2A_\delta^k N^{3r+3k}
        e^{N[k\omega(\delta)+(r-k)\log B]}.
\]
Repeated occurrences of a face are still constrained by one target; the argument sums only selections satisfying that target. The CROSS projection retains the whole signed continuant at each permitted original input/output interval, so its coefficients satisfy the same bounds.

If more than \(k\) coordinates are near \(+2\), the exponential rate decreases provided \(\omega(\delta)\le\log B\). Polynomial factors can be enlarged uniformly over the finitely many subsets. The source note now explicitly includes this inequality in its sufficient choice of \(\delta\), together with its strict comparison to the drilled action. Both conditions hold for all sufficiently small positive \(\delta\).

## 3. Restricting the exact angular formula

Let \(E\) be any subset of the distinct spectral roots. A double root must retain both angular representatives
\[
 \phi,\quad2\pi-\phi,\qquad c=2\cos\phi.
\]
The odd simple root, if retained, contributes only \(\phi=\pi\). These conventions turn the restriction of the original Hermite formula into a subset of the original midpoint rows:
\[
 \mathcal L_{N,E}^{n}H
 =-\frac1{N^2}\sum_{\phi\in\widetilde E}
 \left(\cos\phi\,fP+\sin\phi\,f'P+\sin\phi\,fP'\right),
 \qquad P(\phi)=H(2\cos\phi).
\]
There are at most \(N\) rows. The primes here are angular derivatives. The original crossing, including its Cartan phase, satisfies
\[
 |f|=1,\qquad |f'|\le |n|N/2.
\]
The exact trigonometric derivative bound gives \(\|P'\|\le d\|P\|\). Therefore the derivative-in-\(H\) part has norm at most \(d/N\), and the value part has norm at most \(1/N+|n|/2\). Their sum is \(1+|n|/2\). No cancellation between retained and omitted root terms is needed for this inequality.

At roots in \(I_\delta=[2-\delta,2]\), the polynomial derivative is instead bounded on that same interval:
\[
 \|H'\|_{I_\delta}\le2d^2\|H\|_{I_\delta}/\delta.
\]
Since \(4-c^2\le4\delta\) and there are at most \(N/2\) distinct double roots, the derivative part has norm at most \(4d^2/N\). The value part retains the preceding bound. The simple root \(-2\) is outside this interval for \(0<\delta\le1\); it remains in the complementary root set.

These inequalities extend coordinate by coordinate to the mixed rectangle. At an unrestricted coordinate the bound uses the whole interval \([-2,2]\), exactly as specified by that rectangle; it does not assert a bound from the supremum over a disconnected root subset alone.

## 4. The vanished all-value tensor and geometric comparison

The exact shared polynomial \(D_N\) vanishes on the entire product node grid. Thus the tensor product consisting only of value parts vanishes, even when each coordinate is restricted to one of the two root sets. Expanding the exact functionals before estimating gives
\[
 \left[\prod_e(a_e+b_e)-\prod_e b_e\right]\|D_N\|_{\mathcal Q_J},
\]
with precisely the \(a_e,b_e\) in the source note. Mixed normal derivatives remain. There is no derivative of a cutoff or an omitted boundary term, because the restriction is a finite selection of fixed nodes.

The sets \(E_+\) and \(E_-\) partition the original root set, so the tensor terms indexed by subsets \(J\) are disjoint parts of the original finite filling formula. Summing over \(|J|\ge k\) costs only a fixed combinatorial factor. For fixed powers, all functional prefactors are polynomial in \(N\).

If
\[
 (r-k)\log B<\Phi,
\]
one can choose fixed \(\delta>0\) with \(\omega(\delta)\le\log B\) and
\[
 k\omega(\delta)+(r-k)\log B<\Phi.
\]
The established all-CROSS action for the same marked diagram tends to \(\Phi\) under independently long fixed fillings. These mixed regions are therefore strictly below its nonzero contribution once the fillings are sufficiently long. Configurations with fewer than \(k\) positive-end coordinates remain outside this result. Nothing here proves a bound for their sum or the full knot invariant.
