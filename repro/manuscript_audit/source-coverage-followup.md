# Follow-up: full-source coverage, parity, and the planar dependency order

This is a bounded proof-dependency read of the current manuscript, beginning at commit `2cb9c0b2df1bff875eebeadcb75c3cdbaf6fc8de` and including the uncommitted text identified in the accompanying snapshot. It reads the actual formulas and their stated inputs. It does not rerun the exact certificates, reconstruct every quantum-group matrix identity, or repeat the metric-completion audits. No manuscript statement was edited during this read.

The Appendix N and Chapter 9 references were checked again against the hashes in this snapshot. N's canonical-remainder insertion is already present in that file: its section `uf:sec-canonical-reduction` occupies lines 122–208, and the repeated-root section begins at line 210. The references below concern the existing source, Hermite, norm and transfer arguments at their current positions; this follow-up does not claim a fresh audit of the inserted canonical-remainder proof. Chapter 9's final scope section now begins at line 258. Exact TeX labels are included where available; line numbers describe only this snapshot.

## 1. Conclusion and action required

No new scope defect or circular full-source assumption was found in the inspected chain. The recursive Conway construction has its own signed complementary-color theorem. Its proof does not depend on an unresolved bound for the general matched-sphere source. The latter generality has a smaller, explicitly stated conclusion: Appendix O proves the nonzero geometric contribution, while the complementary part still requires a separate estimate.

The full-invariant conclusions in Appendices L and P do supply that separate estimate under their respective hypotheses. They do not obtain it merely from Appendix O or from the finite filling norm in N. Their estimates and the geometric-contribution theorem run through both level parities. The odd-level real-stability results used in the separate cap research are not premises of these all-level manuscript statements.

There is no essential replacement paragraph to recommend from this read. The restrictions listed below must remain visible in any summary: completed-root grammar for the recursive theorem; actual finite decoration for L; weak balance or its explicit quantified alternative for P; geometric contribution only for a general unchanged sphere. The distinction is presently explicit in `01-introduction.tex:18–55, 144–160`, `09-reproduction.tex:70–105, 258–298` (the paragraphs after `prop:volume-rate-transfer` and the section “The scope of the conclusions”), and `main.tex:60–82`.

## 2. The recursive theorem supplies its own global signed estimate

The exact scope is `01-introduction.tex:126–160`: every completed box begins with an `hh` seed, further operations are precisely the displayed grammar, and both children of the final cylindrical closure are completed. The parity pattern must yield one knot without an internally closed main component. All powers and the finite expression are fixed before the level limit. This is a specified arborescent family, not every Conway or arborescent knot.

The final two-child condition has an analytic purpose. `03-entropy.tex:150–168` gives the selected leaf interval

\[
  \frac14<a_\ell<\frac{\arctan2}{\pi},
\]

with a compact subinterval for each fixed expression. It is not a tree-independent compact interval. This is the high-index input to the selected-source packet.

The signed global bound is a different theorem from that local packet:

- `02-finite-source.tex:206–233` retains the exact high-color core/alias decomposition and the full triangular half-twist transport. A half-twisted alias may occupy all Newton coordinates.
- `B2-global-core-envelope.tex:15–71` keeps the true physical lower endpoint, the nonzero complete normalization and the actual upper wall at both parities. The two terminal moduli are explicitly different and both bounded by one.
- `B2:82–123, 153–223` controls both recurrence roots, including collisions. Fixed-block Cayley–Hamilton bounds are used before taking a long product; no uniform eigenvector basis is assumed. The singular small-index interval is bounded separately and its rate cost tends to zero with that interval.
- `B2:225–318` converts this into the uniform core envelope and the full-range alias bound. It does not replace a uniform exponential-rate core bound by a polynomial prefactor at collisions.
- `05-alias.tex:27–31, 49–74, 86–139` uses the full multiplication tetrahedron, not an all-low truncation. The two finite supporting-plane certificates and the elementary leaf interval estimate provide the stated fixed margins. The inherited child keeps its affine output tangent over its whole output range.
- `05:143–184` performs the whole-tree induction. Completed products cancel internal tangent coefficients; turns retain the exact affine offset from `d=N−1`; an inherited loss is not charged again. There are finitely many sectors and polynomially many states for the fixed tree. Uniform rate errors are absorbed only after fixing the positive margins.

The resulting bounds are `eq:whole-alias-gap` and `eq:physical-color-gap`. They do not invoke the general Morse left/right remainder estimate. Moreover the tree core/alias split is not the same sector decomposition as the central/left/right path split of Appendix O. A difficulty for an arbitrary matched-sphere central complement is therefore not, by itself, a missing hypothesis in this induction.

The finite Newton multiplication, turn, circle and normal identities in Appendix A remain substantive inputs. This read checked their use and the displayed support identities; it did not independently rebuild every defining crossing matrix. The exact rational certificate data are also proof inputs. Their global supporting-plane/interval logic was reread here; their arithmetic replay is a separate recorded computation.

## 3. Passage from the tree estimate to the whole filled invariant

`06-packet.tex:14–30` defines the packet by the exact finite wire sum before introducing index interpolation. The later local asymptotic is not used to bound discarded colors. `06:77–113` retains the primitive lattice offsets, the nonzero complete multiplier, the negative color Hessian and the comparison error to the original source. Appendix B1 remains the detailed source-selected recurrence and exponential interpolation proof.

`08-filling.tex:16, 49–84` first transports the global error with the exact polynomial coefficient-mass bound, then folds only the even retained corridor. Its sampled total derivative includes the repeated-root normal. The zero charge disappears by the actual endpoint zeros, not by deleting a formal mode.

The charge proof retains the required distinctions:

- `08:90–118` controls tails with paired endpoint currents while spectator chirps stay real. The estimate costs powers of fixed slopes, not exponentials in another cusp's slope.
- `08:153–174` compares local critical values in independent variables `1/p_i` and `m_i/p_i`. The strict comparison integrates derivatives in the squared charge ratios; it does not presume comparable slopes.
- `B-analytic-estimates.tex:10–35` establishes the complex Fourier strip by inserting the complex parameter into the same cotangent contour. It does not infer preservation of cancellation from a coefficientwise Fourier-support bound.
- `B:63–106` chooses the outer box before the smaller local ratio neighborhood and reciprocal-slope bound. Higher-charge connectors carry an absolute gap below the first-charge contribution; they are not required to have a relative error compared with every smaller higher-charge saddle.
- `08:185–202` shows that the minimal signed charges add exactly and that their coefficient is nonzero. Only then is the fixed twist threshold increased until their selected action exceeds every absolute source and connector error level.

This is the analytic implication needed by the recursive theorem. The actual primitive filling and absolute action/volume equality are the separate Chapter 7/Appendix D inputs. The new elementary transfer proposition in `09:19–68` (`prop:volume-rate-transfer` and its following amplitude paragraph) accurately separates these obligations and correctly keeps the relative `1+O(N^{-1})` term in the main amplitude.

## 4. N/O/P/L form a statement-level acyclic dependency chain

The visible cross-references between appendices do not form a cycle of volume conclusions. The order is as follows.

1. **Initial packing and exact Morse source.** L's initial simple-sphere packing construction and its exact source at `L:500–678` precede any full-invariant restoration. They are available without the later balance argument. O imports these statements, not L's final volume conclusion.
2. **Finite functional bound N.** `N:71–120` (`uf:sec-the-exact-source-and-its-normalization`, equations `uf:eq-5`–`uf:eq-7`) uses only the exact original coefficient identity, spectral degree at most `N−1` in each variable, and full-Hermite crossing data. Its source application starts at `N≥3`; the polynomial norm theorem itself holds at `N≥2`. Neither a geometric certificate nor balance is needed. Its reference to O for the name of the central sector is a definition, not a use of O's asymptotic theorem.
3. **Geometric contribution O.** `O:180–259` checks the original ordinary graph, primitive phase quotient, protected-zero patterns, actual cofactor interpolation and angular complement. `O:128–178` states the local packet/global strip and the nonzero whole-period asymptotic. The dependency table `O:549–628` explicitly excludes the older full-source restoration theorem. The second half supplies the original marked representation, smooth primitive filling and volume calibration. There is no balance assumption in this central contribution.
4. **Strict restoration L.** `L:1303–1334` uses its separately constructed strict complete-radius inequalities, the actual phase-uniform left/right bounds and the central coefficient bound on one shared torus. Every surviving noncentral factor has a strict loss. The original `d` targets and protected zeros are retained. `L:1336–1363` bounds the entire filled remainder and compares it with the independently established first-charge term. The reference to O at line 1347 describes the same central argument already proved in L's preceding sections; it is not needed to prove the packing or source statements imported by O.
5. **Weak restoration P.** `P:146–157` imports only complete stationarity and calibrated action from O. `P:197–212` imports the local envelopes from the proof in L before any use of balance. `P:226–310` then proves a new strict shared-source remainder bound using its common power change of weights. `P:324–369` applies N and O, and increases the fixed twist threshold only after fixing that remainder gap.

In particular, N does not prove a source bound, O does not prove a general complementary bound, and L's final theorem is not an input to its own restoration. These restrictions are also stated explicitly at `N:423–461` (`uf:sec-the-estimate-needed-for-long-fillings`, equations `uf:eq-26`–`uf:eq-29`), `O:524–547`, and `P:371–375`.

## 5. Parity and the possible stable-polynomial confusion

The all-level assertions do not use a blanket claim that every central cofactor is real stable.

`O:222–250` uses the independently anchored local interpolation on both parity grids. It explicitly retains the odd skipping term

\[
 G_bG_c+\omega s_ms_{m+1}xyD_bD_c
\]

and its derivative at `ω=0`; the even source is the original three-cut sum. The local complex neighborhood is around positive geometric face weights with the actual protected zeros. This is not a global stability statement in all upper-half-plane face variables. The angular complement is supplied separately by the actual cofactor theorem and nodal interpolation.

`L:1307` gives the disjoint even and odd path partitions, including the odd zero-step central path once. `N:213–270` (`uf:sec-repeated-roots-the-odd-simple-root-and-the-midpoint-identity`, equations `uf:eq-8`–`uf:eq-15`) includes the odd simple spectral node with its exact weight; `N:353–378` (`uf:sec-shared-polynomials-and-the-unsplit-complementary-source`, equations `uf:eq-24`–`uf:eq-25` and the proof of `uf:eq-4`) uses joint product-grid vanishing, not the stronger and generally false assertion of vanishing on every spectral node hyperplane. `P:275–310` preserves degree at most `d=N−1` in each spectral variable and explicitly covers both parities.

No dependency on the separate odd stable-exterior cap criterion, its common-negative-axis estimate, or a spectral-neighbor extension was found in this chain. The unresolved even or neighboring-spectrum extensions of those cap methods therefore do not remove a stated premise from these particular manuscript proofs. This conclusion does not certify a different source class or fill a missing general remainder bound.

## 6. Limits of this follow-up

The read is a proof-level check of the displayed source estimates, assembly and their scope. It is not a fresh complete proof of the external cofactor packet/interpolation theorems, a new arithmetic replay, or a reconstruction of every topology and metric lemma. Those named dependencies remain in the snapshot and in the earlier bounded records. No claim is made that the entire paper is formally verified.

For an arbitrary unchanged matched sphere failing all presently supplied remainder criteria, the exact missing step remains an estimate or coherent cancellation argument for the original full-minus-central contribution after its common face extraction. The manuscript does not assert that this step is solved. Nothing in the present read promotes an odd fixed-spectrum cap estimate to a full, all-parity, all-spectrum knot-volume theorem.
